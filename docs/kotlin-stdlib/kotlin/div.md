

# div

Enables the use of the / operator for BigDecimal instances.

```kotlin
inline operator fun BigDecimal.div(other: BigDecimal): BigDecimal(source)
```

```kotlin
import java.math.BigDecimal

fun main() {
    val numerator = BigDecimal("10")
    val denominator = BigDecimal("3")
    val quotient = numerator / denominator
    println("10 / 3 = $quotient")  // Prints: 10 / 3 = 3.333333333333333333333333333
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/div.html)

    