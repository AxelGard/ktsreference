

# toLongOrNull

Parses the string to a Long number or returns null if the string is not a valid representation of a Long.

```kotlin
fun String.toLongOrNull(): Long?(source)
```

```kotlin
fun main() {
    val validString  = "9876543210"
    val invalidString = "not_a_number"

    val validNumber: Long?   = validString.toLongOrNull()
    val invalidNumber: Long? = invalidString.toLongOrNull()

    println("Valid number: $validNumber")   // prints: Valid number: 9876543210
    println("Invalid number: $invalidNumber") // prints: Invalid number: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-long-or-null.html)

    