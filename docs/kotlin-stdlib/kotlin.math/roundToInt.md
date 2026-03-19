

# roundToInt

Rounds this Double value to the nearest integer and converts the result to Int. Ties are rounded towards positive infinity.

```kotlin
expect fun Double.roundToInt(): Int(source)
```

```kotlin
import kotlin.math.roundToInt

fun main() {
    val values = listOf(3.5, 3.4, -3.5)
    values.forEach { value ->
        println("$value rounded to Int is ${value.roundToInt()}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/round-to-int.html)

    