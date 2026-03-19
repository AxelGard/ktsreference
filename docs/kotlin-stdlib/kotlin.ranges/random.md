

# random

Returns a random element from this range.

```kotlin
inline fun IntRange.random(): Int(source)
```

```kotlin
import kotlin.random.Random

fun main() {
    val randomNumber = 1..10 random(Random.Default)
    println("Random number between 1 and 10: $randomNumber")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.ranges/random.html)

    