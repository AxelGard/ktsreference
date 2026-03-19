

# truncate

Rounds the given value x to an integer towards zero.

```kotlin
expect fun truncate(x: Double): Double(source)
```

```kotlin
import kotlin.math.truncate

fun main() {
    val values = listOf(3.7, -3.7, 0.0, 5.0, -2.3)

    for (v in values) {
        println("truncate($v) = ${truncate(v)}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/truncate.html)

    