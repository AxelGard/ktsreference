

# substringAfter

Returns a substring after the first occurrence of delimiter. If the string does not contain the delimiter, returns missingDelimiterValue which defaults to the original string.

```kotlin
fun String.substringAfter(delimiter: Char, missingDelimiterValue: String = this): String(source)
```

```kotlin
fun main() {
    val text1 = "Hello,World".substringAfter(',')
    println(text1)          // Output: World

    val text2 = "HelloWorld".substringAfter(',')
    println(text2)          // Output: HelloWorld (missing delimiter, returns original)

    val text3 = "HelloWorld".substringAfter(',', "No comma found")
    println(text3)          // Output: No comma found (custom missing value)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/substring-after.html)

    