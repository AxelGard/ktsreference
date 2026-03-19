

# round

Rounds the given value x towards the closest integer with ties rounded towards even integer.

```kotlin
expect fun round(x: Double): Double(source)
```

```kotlin
import kotlin.math.round

fun main() {
    val values = listOf(2.5, 3.5, 1.2, 4.8)

    for (v in values) {
        println("round($v) = ${round(v)}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/round.html)

    