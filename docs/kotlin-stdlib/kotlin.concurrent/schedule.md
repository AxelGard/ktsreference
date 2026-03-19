

# schedule

Schedules an action to be executed after the specified delay (expressed in milliseconds).

```kotlin
inline fun Timer.schedule(delay: Long, crossinline action: TimerTask.() -> Unit): TimerTask(source)
```

```kotlin
import java.util.Timer
import kotlin.concurrent.schedule

fun main() {
    val timer = Timer()
    timer.schedule(2000) {
        println("Task executed after 2 seconds")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/schedule.html)

    