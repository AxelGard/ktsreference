

# toUByteOrNull

Parses the string as an UByte number and returns the result or null if the string is not a valid representation of a number.

```kotlin
fun String.toUByteOrNull(): UByte?(source)
```

```kotlin
fun main() {
    val validString = "150"
    val invalidString = "300"   // outside UByte range 0..255

    val validUByte = validString.toUByteOrNull()
    val invalidUByte = invalidString.toUByteOrNull()

    println("Valid string result: $validUByte")   // Prints: 150
    println("Invalid string result: $invalidUByte") // Prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-u-byte-or-null.html)

    