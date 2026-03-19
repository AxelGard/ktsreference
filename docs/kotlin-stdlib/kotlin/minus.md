

# minus

Enables the use of the - operator for BigDecimal instances.

```kotlin
inline operator fun BigDecimal.minus(other: BigDecimal): BigDecimal(source)
```

```kotlin
import java.math.BigDecimal

fun main() {
    val total = BigDecimal("150.00")
    val tax   = BigDecimal("20.00")

    val amountDue = total - tax   // Uses BigDecimal.minus

    println("Amount due: $amountDue")   // Output: Amount due: 130.00
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/minus.html)

    