

# exp

Computes Euler's number e raised to the power of the value x.

```kotlin
expect fun exp(x: Double): Double(source)
```

```kotlin
import kotlin.math.exp

fun main() {
    val power = 2.0
    val result = exp(power)          // e^2.0
    println("e^$power = $result")    // prints: e^2.0 = 7.389056098930649
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/exp.html)

    