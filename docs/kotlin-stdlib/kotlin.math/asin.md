

# asin

Computes the arc sine of the value x; the returned value is an angle in the range from -PI/2 to PI/2 radians.

```kotlin
expect fun asin(x: Double): Double(source)
```

```kotlin
import kotlin.math.asin
import kotlin.math.PI

fun main() {
    val value = 0.5           // input in the range [-1.0, 1.0]
    val radians = asin(value) // result in radians, between -π/2 and π/2
    val degrees = radians * 180.0 / PI

    println("asin($value) = $radians radians")
    println("asin($value) = $degrees degrees")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/asin.html)

    