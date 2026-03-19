

# cos

Computes the cosine of the angle x given in radians.

```kotlin
expect fun cos(x: Double): Double(source)
```

```kotlin
import kotlin.math.cos
import kotlin.math.PI

fun main() {
    val angle = PI / 3   // 60° in radians
    val cosineValue = cos(angle)
    println("cos(60°) = $cosineValue")   // prints 0.5
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/cos.html)

    