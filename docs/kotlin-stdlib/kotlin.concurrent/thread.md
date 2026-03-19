

# thread

Creates a thread that runs the specified block of code.

```kotlin
fun thread(start: Boolean = true, isDaemon: Boolean = false, contextClassLoader: ClassLoader? = null, name: String? = null, priority: Int = -1, block: () -> Unit): Thread(source)
```

```kotlin
import kotlin.concurrent.thread

fun main() {
    // Create and start a new thread that prints numbers 1 to 5
    val worker = thread(name = "worker") {
        for (i in 1..5) {
            println("Worker thread $i")
            Thread.sleep(500) // pause for half a second
        }
    }

    // Wait for the worker thread to finish
    worker.join()
    println("Main thread finished")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/thread.html)

    