

# toBigDecimalOrNull

Parses the string as a java.math.BigDecimal number and returns the result or null if the string is not a valid representation of a number.

```kotlin
fun String.toBigDecimalOrNull(): BigDecimal?(source)
```

```kotlin
import java.math.BigDecimal

fun main() {
    // Valid number string
    val valid = "1234.56".toBigDecimalOrNull()
    println(valid)           // Output: 1234.56

    // Invalid number string
    val invalid = "abc".toBigDecimalOrNull()
    println(invalid)         // Output: null

    // Safe usage with let
    "42".toBigDecimalOrNull()?.let { number ->
        println("Parsed BigDecimal: $number")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-big-decimal-or-null.html)

    