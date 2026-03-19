

# asJavaRandom

Creates a java.util.Random instance that uses the specified Kotlin Random generator as a randomness source.

```kotlin
fun Random.asJavaRandom(): Random(source)
```

```kotlin
import kotlin.random.Random
import java.util.Random as JavaRandom

fun main() {
    // Create a Kotlin Random instance with a fixed seed
    val kotlinRandom = Random(1234L)

    // Convert it to a Java Random that delegates to the same source
    val javaRandom: JavaRandom = kotlinRandom.asJavaRandom()

    // Use the Java Random just like any other java.util.Random
    val randomInt = javaRandom.nextInt(100)          // 0 until 99
    val randomDouble = javaRandom.nextDouble()      // 0.0 until 1.0
    val randomBoolean = javaRandom.nextBoolean()    // true or false

    println("Int: $randomInt, Double: $randomDouble, Boolean: $randomBoolean")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.random/as-java-random.html)

    