

# intercepted

Intercepts this continuation with ContinuationInterceptor.

```kotlin
expect fun <T> Continuation<T>.intercepted(): Continuation<T>(source)
```

```kotlin
import kotlinx.coroutines.*
import kotlin.coroutines.*

// A simple interceptor that logs every resumption
class LoggingInterceptor : ContinuationInterceptor {
    override val key: CoroutineContext.Key<*> = ContinuationInterceptor.Key

    override fun <T> interceptContinuation(continuation: Continuation<T>): Continuation<T> =
        object : Continuation<T> by continuation {
            override suspend fun resumeWith(result: Result<T>) {
                println("LoggingInterceptor: resuming with $result")
                continuation.resumeWith(result)
            }
        }
}

fun main() = runBlocking {
    // Build a coroutine context that contains the interceptor
    val ctx = coroutineContext + LoggingInterceptor()

    // Create a raw continuation with that context
    val cont: Continuation<Unit> = Continuation(ctx) { /* no-op completion */ }

    // Intercept the continuation (applies the interceptor from the context)
    val intercepted = cont.intercepted()

    // Resume the intercepted continuation – the interceptor will log the event
    intercepted.resume(Unit)
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines.intrinsics/intercepted.html)

    