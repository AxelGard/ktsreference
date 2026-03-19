

# measureTime

Executes the given function block and returns the duration of the elapsed time interval.

```kotlin
inline fun measureTime(block: () -> Unit): Duration(source)
```

```kotlin
import kotlin.time.*
import kotlin.time.DurationUnit.*
import kotlin.time.toDuration

fun main() {
    val duration = measureTime {
        // Simulate work
        Thread.sleep(500)
    }

    println("Elapsed time: ${duration.toDouble(DurationUnit.MILLISECONDS)} ms")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/measure-time.html)

    