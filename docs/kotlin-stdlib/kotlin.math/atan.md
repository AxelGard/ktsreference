

# atan

Computes the arc tangent of the value x; the returned value is an angle in the range from -PI/2 to PI/2 radians.

```kotlin
expect fun atan(x: Double): Double(source)
```

```kotlin
import kotlin.math.atan
import kotlin.math.PI

fun main() {
    val value = 1.0
    val angleInRadians = atan(value)
    val angleInDegrees = angleInRadians * 180 / PI

    println("atan($value) = $angleInRadians radians")
    println("atan($value) = $angleInDegrees degrees")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/atan.html)

    