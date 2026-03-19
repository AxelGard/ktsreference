

# getTimeNanos

Warning since 1.9

```kotlin
external fun getTimeNanos(): Long(source)
```

```kotlin
import kotlin.system.getTimeNanos

fun main() {
    val start = getTimeNanos()
    // Simulate some work
    Thread.sleep(500)
    val end = getTimeNanos()

    val elapsedMillis = (end - start) / 1_000_000
    println("Elapsed time: $elapsedMillis ms")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.system/get-time-nanos.html)

    