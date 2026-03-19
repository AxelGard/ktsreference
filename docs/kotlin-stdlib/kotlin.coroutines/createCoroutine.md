

# createCoroutine

Creates a coroutine without a receiver and with result type T. This function creates a new, fresh instance of suspendable computation every time it is invoked.

```kotlin
fun <T> suspend () -> T.createCoroutine(completion: Continuation<T>): Continuation<Unit>(source)
```

```kotlin
import kotlin.coroutines.*

fun main() {
    // A suspend lambda that returns a String
    val suspendable: suspend () -> String = {
        "Hello from createCoroutine!"
    }

    // Create a coroutine from the suspend lambda
    val continuation = suspendable.createCoroutine(object : Continuation<String> {
        override val context = EmptyCoroutineContext
        override fun resumeWith(result: Result<String>) {
            println("Coroutine finished with: ${result.getOrNull()}")
        }
    })

    // Start the coroutine by resuming it with Unit
    continuation.resume(Unit)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/create-coroutine.html)

    