

# tanh

Computes the hyperbolic tangent of the value x.

```kotlin
expect fun tanh(x: Double): Double(source)
```

import kotlin.math.tanh

fun main() {
    val values = listOf(-2.0, 0.0, 2.0)
    for (v in values) {
        println("tanh($v) = ${tanh(v)}")
    }
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/tanh.html)

    