

# dec

Enables the use of the unary -- operator for BigDecimal instances.

```kotlin
inline operator fun BigDecimal.dec(): BigDecimal(source)
```

```kotlin
import java.math.BigDecimal

fun main() {
    var amount = BigDecimal("100.00")
    println("Before decrement: $amount")   // 100.00
    amount--
    println("After decrement:  $amount")   // 99.00
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/dec.html)

    