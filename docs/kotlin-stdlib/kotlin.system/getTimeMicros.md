

# getTimeMicros

Warning since 1.9

```kotlin
external fun getTimeMicros(): Long(source)
```

```kotlin
import kotlin.system.getTimeMicros

fun main() {
    val start = getTimeMicros()
    // ... code you want to time ...
    val duration = getTimeMicros() - start
    println("Execution time: $duration µs")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.system/get-time-micros.html)

    