

# toTimeUnit

Converts this kotlin.time.DurationUnit enum value to the corresponding java.util.concurrent.TimeUnit value.

```kotlin
fun DurationUnit.toTimeUnit(): TimeUnit(source)
```

```kotlin
import java.util.concurrent.TimeUnit
import kotlin.time.DurationUnit

fun main() {
    val kotlinUnit = DurationUnit.MINUTES
    val javaUnit: TimeUnit = kotlinUnit.toTimeUnit()
    println("Converted $kotlinUnit to $javaUnit")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/to-time-unit.html)

    