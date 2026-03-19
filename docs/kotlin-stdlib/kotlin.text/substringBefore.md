

# substringBefore

Returns a substring before the first occurrence of delimiter. If the string does not contain the delimiter, returns missingDelimiterValue which defaults to the original string.

```kotlin
fun String.substringBefore(delimiter: Char, missingDelimiterValue: String = this): String(source)
```

```kotlin
fun main() {
    val text1 = "Hello,World"
    val beforeComma = text1.substringBefore(',')
    println(beforeComma) // prints "Hello"

    val text2 = "Hello"
    val beforeCommaWithDefault = text2.substringBefore(',', "N/A")
    println(beforeCommaWithDefault) // prints "N/A"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/substring-before.html)

    