
build:
	python3 collect.py ./kotlin_stdlib_urls.json

deploy:
	mkdocs gh-deploy --force