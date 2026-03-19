

# startCoroutine

Starts a coroutine without a receiver and with result type T. This function creates and starts a new, fresh instance of suspendable computation every time it is invoked. The completion continuation is invoked when the coroutine completes with a result or an exception.

```kotlin
fun <T> suspend () -> T.startCoroutine(completion: Continuation<T>)(source)
```

```kotlin
import kotlin.coroutines.*
import kotlin.coroutines.intrinsics.*

fun main() {
    val suspendFunc: suspend () -> String = {
        // Some suspendable work
        "Hello from coroutine!"
    }

    suspendFunc.startCoroutine(object : Continuation<String> {
        override val context: CoroutineContext = EmptyCoroutineContext

        override fun resumeWith(result: Result<String>) {
            result.fold(
                onSuccess = { println("Success: $it") },
                onFailure = { println("Failure: ${it.message}") }
            )
        }
    })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/start-coroutine.html)

    