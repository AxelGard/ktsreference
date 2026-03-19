

# acos

Computes the arc cosine of the value x; the returned value is an angle in the range from 0.0 to PI radians.

```kotlin
expect fun acos(x: Double): Double(source)
```

```kotlin
import kotlin.math.acos

fun main() {
    val x = 0.5
    val angleInRadians = acos(x)
    println("acos($x) = $angleInRadians radians")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/acos.html)

    