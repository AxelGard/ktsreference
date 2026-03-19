

# resumeWithException

Resumes the execution of the corresponding coroutine so that the exception is re-thrown right after the last suspension point.

```kotlin
inline fun <T> Continuation<T>.resumeWithException(exception: Throwable)(source)
```

```kotlin
import kotlinx.coroutines.*
import kotlin.coroutines.*

suspend fun fail(): Int = suspendCancellableCoroutine { cont ->
    // Resume the coroutine with an exception
    cont.resumeWithException(RuntimeException("Something went wrong"))
}

fun main() = runBlocking {
    try {
        fail()
    } catch (e: Throwable) {
        println("Caught exception: ${e.message}")
    }
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/resume-with-exception.html)

    