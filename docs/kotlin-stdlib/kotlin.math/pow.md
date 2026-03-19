

# pow

Raises this value to the power x.

```kotlin
expect fun Double.pow(x: Double): Double(source)
```

```kotlin
import kotlin.math.pow

fun main() {
    val base = 2.0
    val exponent = 3.0
    val result = base.pow(exponent)   // 8.0
    println("$base ^ $exponent = $result")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/pow.html)

    