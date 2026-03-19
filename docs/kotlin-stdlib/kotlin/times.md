

# times

Enables the use of the * operator for BigDecimal instances.

```kotlin
inline operator fun BigDecimal.times(other: BigDecimal): BigDecimal(source)
```

```kotlin
import java.math.BigDecimal

fun main() {
    val pricePerUnit = BigDecimal("19.99")
    val quantity = BigDecimal("3")

    val totalPrice = pricePerUnit * quantity

    println("Total price: $totalPrice")  // Total price: 59.97
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/times.html)

    