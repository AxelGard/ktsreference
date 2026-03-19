

# nextInt

Gets the next random Int from the random number generator in the specified range.

```kotlin
fun Random.nextInt(range: IntRange): Int(source)
```

```kotlin
import kotlin.random.Random

fun main() {
    val randomNumber = Random.nextInt(1..10)
    println("Random number between 1 and 10: $randomNumber")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.random/next-int.html)

    