

# log2

Computes the binary logarithm (base 2) of the value x.

```kotlin
expect fun log2(x: Double): Double(source)
```

```kotlin
import kotlin.math.log2

fun main() {
    val numbers = listOf(1.0, 2.0, 4.0, 8.0, 16.0)

    for (x in numbers) {
        val result = log2(x)
        println("log2($x) = $result")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/log2.html)

    