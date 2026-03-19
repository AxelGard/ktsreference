

# log

Computes the logarithm of the value x to the given base.

```kotlin
expect fun log(x: Double, base: Double): Double(source)
```

```kotlin
import kotlin.math.log

fun main() {
    val value = 8.0
    val base = 2.0
    val result = log(value, base)
    println("log_$base($value) = $result") // prints: log_2.0(8.0) = 3.0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/log.html)

    