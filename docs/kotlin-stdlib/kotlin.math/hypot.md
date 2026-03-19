

# hypot

Computes sqrt(x^2 + y^2) without intermediate overflow or underflow.

```kotlin
expect fun hypot(x: Double, y: Double): Double(source)
```

```kotlin
import kotlin.math.hypot

fun main() {
    val x = 3.0
    val y = 4.0
    val distance = hypot(x, y)
    println("The distance is $distance") // outputs 5.0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/hypot.html)

    