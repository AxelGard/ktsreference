

# replaceAfterLast

Replace part of string after the last occurrence of given delimiter with the replacement string. If the string does not contain the delimiter, returns missingDelimiterValue which defaults to the original string.

```kotlin
fun String.replaceAfterLast(delimiter: String, replacement: String, missingDelimiterValue: String = this): String(source)
```

```kotlin
fun main() {
    val path = "/usr/local/bin/script.sh"
    val updated = path.replaceAfterLast("/", "_v2.sh")
    println(updated)          // prints: /usr/local/bin/script_v2.sh

    val single = "filename"
    val unchanged = single.replaceAfterLast("/", "_new.txt")
    println(unchanged)        // prints: filename
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace-after-last.html)

    