

# measureNanoTime

Executes the given block and returns elapsed time in nanoseconds. For a more human-readable and typed output, measureTime can be used instead.

```kotlin
inline fun measureNanoTime(block: () -> Unit): Long(source)
```

```kotlin
import kotlin.system.measureNanoTime

fun main() {
    val elapsedTime = measureNanoTime {
        // Code you want to time
        val sum = (1..1_000_000).sum()
        println("Sum = $sum")
    }

    println("Elapsed time: $elapsedTime ns")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.system/measure-nano-time.html)

    