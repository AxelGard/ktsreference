

# inc

Enables the use of the unary ++ operator for BigDecimal instances.

```kotlin
inline operator fun BigDecimal.inc(): BigDecimal(source)
```

```kotlin
import java.math.BigDecimal

fun main() {
    var balance = BigDecimal("100.00")
    println("Before increment: $balance")   // 100.00
    balance++                                 // uses BigDecimal.inc()
    println("After increment: $balance")    // 101.00
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/inc.html)

    