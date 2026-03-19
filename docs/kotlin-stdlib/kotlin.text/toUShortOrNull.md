

# toUShortOrNull

Parses the string as an UShort number and returns the result or null if the string is not a valid representation of a number.

```kotlin
fun String.toUShortOrNull(): UShort?(source)
```

```kotlin
fun main() {
    val numberString = "12345"
    val result: UShort? = numberString.toUShortOrNull()
    println(result)          // Prints: 12345

    val badString = "abc"
    val badResult: UShort? = badString.toUShortOrNull()
    println(badResult)       // Prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-u-short-or-null.html)

    