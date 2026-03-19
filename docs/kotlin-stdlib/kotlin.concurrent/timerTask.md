

# timerTask

Wraps the specified action in a TimerTask.

```kotlin
inline fun timerTask(crossinline action: TimerTask.() -> Unit): TimerTask(source)
```

```kotlin
import java.util.Timer
import java.util.TimerTask
import kotlin.concurrent.timerTask

fun main() {
    val timer = Timer()

    // Create a TimerTask that prints a message every second
    val task: TimerTask = timerTask {
        println("Timer tick at ${java.util.Date()}")
    }

    // Schedule the task: start immediately, repeat every 1000 ms
    timer.schedule(task, 0L, 1000L)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/timer-task.html)

    