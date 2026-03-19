

# withWorker

Executes block with new Worker as resource, by starting the new worker, calling provided block (in current context) with newly started worker as this and terminating worker after the block completes. Note that this operation is pretty heavyweight, use preconfigured worker or worker pool if need to execute it frequently.

```kotlin
@ObsoleteWorkersApiinline fun <R> withWorker(name: String? = null, errorReporting: Boolean = true, block: Worker.() -> R): R(source)
```

```kotlin
import kotlin.native.concurrent.Worker
import kotlin.native.concurrent.withWorker

fun main() {
    // Run a simple task in a dedicated worker
    val result = withWorker("MyWorker") {
        // This block runs inside the worker context
        val threadName = Thread.currentThread().name
        "Hello from $threadName!"
    }

    println(result)   // → Hello from MyWorker@<hash>!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.concurrent/with-worker.html)

    