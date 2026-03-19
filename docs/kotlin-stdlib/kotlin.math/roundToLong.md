

# roundToLong

Rounds this Double value to the nearest integer and converts the result to Long. Ties are rounded towards positive infinity.

```kotlin
expect fun Double.roundToLong(): Long(source)
```

```kotlin
import kotlin.math.roundToLong

fun main() {
    val values = listOf(3.6, 2.3, -1.5, -2.5)
    values.forEach { v ->
        println("$v rounded to Long = ${v.roundToLong()}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/round-to-long.html)

    