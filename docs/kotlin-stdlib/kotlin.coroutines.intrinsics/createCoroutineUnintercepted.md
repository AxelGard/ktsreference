

# createCoroutineUnintercepted

Creates unintercepted coroutine without receiver and with result type T. This function creates a new, fresh instance of suspendable computation every time it is invoked.

```kotlin
expect fun <T> suspend () -> T.createCoroutineUnintercepted(completion: Continuation<T>): Continuation<Unit>(source)
```

```kotlin
import kotlin.coroutines.*
import kotlin.coroutines.intrinsics.createCoroutineUnintercepted

suspend fun compute(): Int = 42

fun main() {
    // Suspend lambda that calls the suspend function
    val suspendLambda: suspend () -> Int = { compute() }

    // Create an unintercepted coroutine from the suspend lambda
    val coroutine = suspendLambda.createCoroutineUnintercepted(object : Continuation<Int> {
        override val context = EmptyCoroutineContext
        override fun resumeWith(result: Result<Int>) {
            // This block runs when the coroutine completes
            println("Result: ${result.getOrThrow()}")
        }
    })

    // Start the coroutine by resuming it with Unit
    coroutine.resume(Unit)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines.intrinsics/create-coroutine-unintercepted.html)

    