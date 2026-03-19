

# floor

Rounds the given value x to an integer towards negative infinity.

```kotlin
expect fun floor(x: Double): Double(source)
```

```kotlin
import kotlin.math.floor

fun main() {
    val values = listOf(3.7, -2.3, 5.0, -0.9)
    values.forEach { v ->
        val rounded = floor(v)   // rounds toward negative infinity
        println("floor($v) = $rounded")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/floor.html)

    