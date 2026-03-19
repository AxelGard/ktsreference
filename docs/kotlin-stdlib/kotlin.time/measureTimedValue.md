

# measureTimedValue

Executes the given function block and returns an instance of TimedValue class, containing both the result of the function execution and the duration of the elapsed time interval.

```kotlin
inline fun <T> measureTimedValue(block: () -> T): TimedValue<T>(source)
```

```kotlin
import kotlin.time.measureTimedValue
import kotlin.time.DurationUnit
import kotlin.time.toDuration

fun main() {
    val timed = measureTimedValue {
        // Code whose execution time you want to measure
        Thread.sleep(200)   // Simulate a 200‑ms task
        "Finished"
    }

    println("Result: ${timed.value}")
    println("Time elapsed: ${timed.duration.inWholeMilliseconds} ms")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/measure-timed-value.html)

    