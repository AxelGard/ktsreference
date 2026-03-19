

# toBigIntegerOrNull

Parses the string as a java.math.BigInteger number and returns the result or null if the string is not a valid representation of a number.

```kotlin
fun String.toBigIntegerOrNull(): BigInteger?(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val validString = "12345678901234567890"
    val bigInt = validString.toBigIntegerOrNull()
    println("Parsed value: $bigInt")   // prints: Parsed value: 12345678901234567890

    val invalidString = "not_a_number"
    val nullResult = invalidString.toBigIntegerOrNull()
    println("Parsed value: $nullResult") // prints: Parsed value: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-big-integer-or-null.html)

    