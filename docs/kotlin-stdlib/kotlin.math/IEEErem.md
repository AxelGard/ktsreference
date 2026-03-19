

# IEEErem

Computes the remainder of division of this value by the divisor value according to the IEEE 754 standard.

```kotlin
inline fun Double.IEEErem(divisor: Double): Double(source)
```

```kotlin
import kotlin.math.IEEErem

fun main() {
    val dividend = 10.0
    val divisor = 3.0

    val remainder = dividend.IEEErem(divisor)
    println("IEEE remainder of $dividend / $divisor is $remainder")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/-i-e-e-erem.html)

    