

# rem

Enables the use of the % operator for BigDecimal instances.

```kotlin
inline operator fun BigDecimal.rem(other: BigDecimal): BigDecimal(source)
```

```kotlin
import java.math.BigDecimal

fun main() {
    val dividend = BigDecimal("10.5")
    val divisor  = BigDecimal("3")
    
    // Using the % operator, which calls BigDecimal.rem
    val remainder = dividend % divisor
    
    println("Remainder of $dividend ÷ $divisor = $remainder")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/rem.html)

    