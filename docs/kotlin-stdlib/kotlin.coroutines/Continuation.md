

# Continuation

Creates a Continuation instance with the given context and implementation of resumeWith method.

```kotlin
inline fun <T> Continuation(context: CoroutineContext, crossinline resumeWith: (Result<T>) -> Unit): Continuation<T>(source)
```

```kotlin
import kotlin.coroutines.*

fun main() {
    // Create a Continuation that prints the result or the error
    val cont: Continuation<Int> = Continuation(EmptyCoroutineContext) { result ->
        result.fold(
            onSuccess = { println("Success: $it") },
            onFailure = { println("Failure: ${it.message}") }
        )
    }

    // Resume the continuation with a successful value
    cont.resumeWith(Result.success(42))

    // Resume the continuation with an exception
    cont.resumeWith(Result.failure(RuntimeException("something went wrong")))
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/-continuation.html)

    