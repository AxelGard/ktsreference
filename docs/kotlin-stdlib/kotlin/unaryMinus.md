

# unaryMinus

Enables the use of the unary - operator for BigDecimal instances.

```kotlin
inline operator fun BigDecimal.unaryMinus(): BigDecimal(source)
```

```kotlin
import java.math.BigDecimal

fun main() {
    val positive = BigDecimal("123.45")
    val negative = -positive   // unary minus
    println(negative)          // prints: -123.45
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/unary-minus.html)

    