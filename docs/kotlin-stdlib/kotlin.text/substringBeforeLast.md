

# substringBeforeLast

Returns a substring before the last occurrence of delimiter. If the string does not contain the delimiter, returns missingDelimiterValue which defaults to the original string.

```kotlin
fun String.substringBeforeLast(delimiter: Char, missingDelimiterValue: String = this): String(source)
```

```kotlin
fun main() {
    val path = "/usr/local/bin/executable"
    val directory = path.substringBeforeLast('/')   // "/usr/local/bin"

    val name = "filename.txt"
    val base = name.substringBeforeLast('.')        // "filename"

    val noDelimiter = "simpleString"
    val unchanged = noDelimiter.substringBeforeLast('-')  // "simpleString"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/substring-before-last.html)

    