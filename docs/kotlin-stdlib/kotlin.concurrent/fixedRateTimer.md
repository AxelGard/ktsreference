

# fixedRateTimer

Creates a timer that executes the specified action periodically, starting after the specified initialDelay (expressed in milliseconds) and with the interval of period milliseconds between the start of the previous task and the start of the next one.

```kotlin
inline fun fixedRateTimer(name: String? = null, daemon: Boolean = false, initialDelay: Long = 0.toLong(), period: Long, crossinline action: TimerTask.() -> Unit): Timer(source)
```

```kotlin
import kotlin.concurrent.fixedRateTimer
import java.util.TimerTask

fun main() {
    var tick = 0
    val timer: java.util.Timer = fixedRateTimer(
        name = "DemoTimer",
        initialDelay = 1_000, // 1 second
        period = 2_000        // 2 seconds
    ) {
        println("Tick $tick")
        tick++
        if (tick >= 5) {
            this.cancel()   // 'this' refers to the TimerTask instance
        }
    }

    // Keep the main thread alive long enough to see the timer ticks
    Thread.sleep(12_000)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/fixed-rate-timer.html)

    