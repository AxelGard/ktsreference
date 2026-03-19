

# Random

Returns a repeatable random number generator seeded with the given seed Int value.

```kotlin
fun Random(seed: Int): Random(source)
```

```kotlin
import kotlin.random.Random

fun main() {
    // Create a repeatable random number generator with a fixed seed
    val rng = Random(12345)

    // Generate some random values
    val randomInt   = rng.nextInt(0, 100)   // 0–99
    val randomLong  = rng.nextLong(1L, 1000L) // 1–999
    val randomFloat = rng.nextFloat()       // 0.0–1.0
    val randomDouble = rng.nextDouble()     // 0.0–1.0

    println("Int: $randomInt")
    println("Long: $randomLong")
    println("Float: $randomFloat")
    println("Double: $randomDouble")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.random/-random.html)

    