

# scheduleAtFixedRate

Schedules an action to be executed periodically, starting after the specified delay (expressed in milliseconds) and with the interval of period milliseconds between the start of the previous task and the start of the next one.

```kotlin
inline fun Timer.scheduleAtFixedRate(delay: Long, period: Long, crossinline action: TimerTask.() -> Unit): TimerTask(source)
```

```kotlin
import java.util.Timer
import kotlin.concurrent.scheduleAtFixedRate

fun main() {
    val timer = Timer()
    timer.scheduleAtFixedRate(delay = 0L, period = 1000L) {
        println("Tick at ${System.currentTimeMillis()}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/schedule-at-fixed-rate.html)

    