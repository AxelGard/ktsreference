

# CancellationException

Creates an instance of CancellationException with the given message and cause.

```kotlin
expect fun CancellationException(message: String?, cause: Throwable?): CancellationException(source)
```

```kotlin
import kotlinx.coroutines.*
import kotlin.coroutines.cancellation.CancellationException

fun main() = runBlocking {
    val job = launch {
        try {
            // Simulate some work
            delay(100)
            // Explicitly cancel this coroutine with a custom CancellationException
            throw CancellationException(
                message = "Cancelled intentionally",
                cause = RuntimeException("Inner error")
            )
        } catch (e: CancellationException) {
            println("Caught cancellation: ${e.message}")
            println("Underlying cause: ${e.cause}")
        }
    }
    job.join()
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines.cancellation/-cancellation-exception.html)

    