import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os 
import sys
import http.client
import json
from tqdm import tqdm

import asyncio
from playwright.async_api import async_playwright

async def get_html(page_url:str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(page_url)
        await page.wait_for_load_state("networkidle")

        html = await page.content()
        await browser.close()
        return html


def ask_llm(question: str, model: str = "deepseek-r1:1.5b") -> str:
    """
    Send a prompt to local Ollama and return the model's answer as a string.
    Uses only Python's standard library.
    """
    conn = http.client.HTTPConnection("192.168.0.228", 11434)

    payload = json.dumps({"model": model, "prompt": question, "stream": False})

    headers = {"Content-Type": "application/json"}

    conn.request("POST", "/api/generate", body=payload, headers=headers)
    response = conn.getresponse()

    if response.status != 200:
        raise RuntimeError(f"Ollama error: {response.status} {response.reason}")

    data = response.read().decode("utf-8")
    conn.close()

    result = json.loads(data)
    return result.get("response", "")

def make_page(url):
    r = requests.get(url,) 
    soup = BeautifulSoup(r.text, features="html.parser")

    found = soup.find_all("h1", {"class":"cover"})
    func_heading = ""
    if len(found) > 0: 
        func_heading = found[0].text
    func_heading

    found = soup.find_all("div", {"class":"breadcrumbs"})
    func_path = ""
    if len(found) > 0: 
        func_path = found[0].text
    func_path

    found = soup.find_all("div", {"class":"symbol monospace"})
    func_sig = ""
    if len(found) > 0: 
        func_sig = found[0].text
    found = soup.find_all("p", {"class": "paragraph"})
    if len(found) > 0: 
        func_doc = found[0].text

    bredcrum = ""
    bpath = func_path.split("/")[:-1]
    for i, crum in enumerate(bpath):
        bredcrum += f"/ [{crum}](/{"/".join(bpath[:i+1])}) "
    bredcrum += f"/ [{func_heading}]({func_path})"
    bredcrum = bredcrum[1:]
    bredcrum

    
    prompt = f"""
    I want you to give me a example usage of the kotlin {func_heading}.

    Here is some info about it: 
    {func_heading}
    {func_path}
    {func_doc}
    {func_sig}
    Source: {url}

    The example will be used for documentation. 
    It should be easy to follow and understand.

    So what would be a simple example usage of {func_sig}
    Only give the code example and nothing else in your response.
    """

    response = ask_llm(prompt, "gpt-oss")


    md_text = f"""

# {func_heading}

{func_doc}

```kotlin
{func_sig}
```

{response}

[Source]({url})

    """

    md_dir = f"./docs/{"/".join(func_path.split("/")[:-1])}" 
    md_file = f"{md_dir}/{func_heading}.md"
    os.system(f"mkdir -p {md_dir}")
    with open(md_file, "w") as f:
        f.write(md_text)
        

def main(args):
    file = args[0]
    with open(file, "r" ) as f:
        urls = json.load(f)
    for url in tqdm(urls):
        try: 
            make_page(url)
        except Exception as e:
            pass

if __name__ == "__main__":
    main(sys.argv[1:])