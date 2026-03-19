

# measureTimeMillis

Executes the given block and returns elapsed time in milliseconds.

```kotlin
inline fun measureTimeMillis(block: () -> Unit): Long(source)
```

```kotlin
import kotlin.system.measureTimeMillis

fun main() {
    val time = measureTimeMillis {
        var sum = 0
        for (i in 1..1_000_000) sum += i
    }
    println("Time taken: $time ms")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.system/measure-time-millis.html)

    