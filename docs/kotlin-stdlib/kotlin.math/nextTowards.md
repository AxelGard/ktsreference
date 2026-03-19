

# nextTowards

Returns the Double value nearest to this value in direction from this value towards the value to.

```kotlin
expect fun Double.nextTowards(to: Double): Double(source)
```

```kotlin
import kotlin.math.nextTowards

fun main() {
    val current = 1.0
    val target  = 2.0

    // Get the next representable Double value in the direction towards the target
    val nextValue = current.nextTowards(target)

    println("Current value: $current")
    println("Target value:  $target")
    println("Next value towards target: $nextValue")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.math/next-towards.html)

    