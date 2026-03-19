

# toDurationUnit

Converts this java.util.concurrent.TimeUnit enum value to the corresponding kotlin.time.DurationUnit value.

```kotlin
fun TimeUnit.toDurationUnit(): DurationUnit(source)
```

```kotlin
import java.util.concurrent.TimeUnit
import kotlin.time.DurationUnit
import kotlin.time.toDuration

fun main() {
    // Java time unit
    val javaUnit = TimeUnit.MINUTES

    // Convert it to Kotlin DurationUnit
    val kotlinUnit: DurationUnit = javaUnit.toDurationUnit()

    // Use the converted unit to create a Duration
    val duration = 10.toDuration(kotlinUnit)

    println(duration)          // prints: 10m
    println(kotlinUnit)        // prints: MINUTES
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/to-duration-unit.html)

    