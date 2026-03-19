

# nextLong

Gets the next random Long from the random number generator in the specified range.

```kotlin
fun Random.nextLong(range: LongRange): Long(source)
```

```kotlin
import kotlin.random.Random

fun main() {
    // Generate a random Long between 1 and 100 (inclusive)
    val randomLong: Long = Random.nextLong(1L..100L)
    println("Random Long: $randomLong")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.random/next-long.html)

    