

# measureTimeMicros

Warning since 1.9

```kotlin
inline fun measureTimeMicros(block: () -> Unit): Long(source)
```

```kotlin
import kotlin.system.measureTimeMicros

fun main() {
    val durationMicros = measureTimeMicros {
        // Code whose execution time you want to measure
        val numbers = (1..1_000_000).toList()
        val sum = numbers.sum()
        println("Sum is $sum")
    }

    println("Execution time: $durationMicros µs")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.system/measure-time-micros.html)

    