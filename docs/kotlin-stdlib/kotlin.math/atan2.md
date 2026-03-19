

# atan2

Returns the angle theta of the polar coordinates (r, theta) that correspond to the rectangular coordinates (x, y) by computing the arc tangent of the value y / x; the returned value is an angle in the range from -PI to PI radians.

```kotlin
expect fun atan2(y: Double, x: Double): Double(source)
```

```kotlin
import kotlin.math.atan2

fun main() {
    val x = 1.0
    val y = 1.0
    val angle = atan2(y, x)
    println("Angle: $angle radians")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/atan2.html)

    