

# times

Returns a duration whose value is the specified duration value multiplied by this number.

```kotlin
inline operator fun Int.times(duration: Duration): Duration(source)
```

```kotlin
import kotlin.time.Duration
import kotlin.time.Duration.Companion.seconds

fun main() {
    val timeout: Duration = 5 * 3.seconds   // 5 * 3 seconds = 15 seconds
    println(timeout)                       // prints "15.0 s"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/times.html)

    