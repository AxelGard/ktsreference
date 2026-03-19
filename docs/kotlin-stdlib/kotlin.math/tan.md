

# tan

Computes the tangent of the angle x given in radians.

```kotlin
expect fun tan(x: Double): Double(source)
```

```kotlin
import kotlin.math.tan
import kotlin.math.PI

fun main() {
    // Angle of 45 degrees in radians
    val angleDegrees = 45.0
    val angleRadians = Math.toRadians(angleDegrees)

    // Compute the tangent
    val tanValue = tan(angleRadians)

    println("tan($angleDegrees°) = $tanValue")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/tan.html)

    