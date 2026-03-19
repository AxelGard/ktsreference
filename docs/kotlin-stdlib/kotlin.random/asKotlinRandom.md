

# asKotlinRandom

Creates a Kotlin Random instance that uses the specified java.util.Random generator as a randomness source.

```kotlin
fun Random.asKotlinRandom(): Random(source)
```

```kotlin
import java.util.Random
import kotlin.random.Random as KotlinRandom

fun main() {
    // Java Random instance
    val javaRandom = Random()

    // Kotlin Random that delegates to the Java Random
    val kotlinRandom: KotlinRandom = javaRandom.asKotlinRandom()

    // Generate a random integer between 0 (inclusive) and 100 (exclusive)
    val randomInt = kotlinRandom.nextInt(0, 100)

    println("Random integer between 0 and 99: $randomInt")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.random/as-kotlin-random.html)

    