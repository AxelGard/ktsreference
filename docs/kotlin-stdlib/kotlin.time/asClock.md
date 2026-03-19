

# asClock

Creates a Clock that uses the time mark at the moment of creation to determine how far the current moment is from the origin.

```kotlin
@JvmName(name = "fromTimeSource")fun TimeSource.asClock(origin: Instant): Clock(source)
```

```kotlin
import kotlin.time.*
import kotlin.time.TimeSource.Monotonic

fun main() {
    val origin = Instant.now()
    val clock = Monotonic.asClock(origin)

    println("Elapsed time from origin: ${clock.elapsedNow()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/as-clock.html)

    