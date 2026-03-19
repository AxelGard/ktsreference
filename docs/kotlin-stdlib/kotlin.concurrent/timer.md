

# timer

Creates a timer that executes the specified action periodically, starting after the specified initialDelay (expressed in milliseconds) and with the interval of period milliseconds between the end of the previous task and the start of the next one.

```kotlin
inline fun timer(name: String? = null, daemon: Boolean = false, initialDelay: Long = 0.toLong(), period: Long, crossinline action: TimerTask.() -> Unit): Timer(source)
```

```kotlin
import java.util.*
import kotlin.concurrent.timer

fun main() {
    val heartbeat = timer(name = "Heartbeat", period = 1000) {
        println("Heartbeat at ${Date()}")
    }

    Thread.sleep(5000)  // let it run for 5 seconds
    heartbeat.cancel()  // stop the timer
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/timer.html)

    