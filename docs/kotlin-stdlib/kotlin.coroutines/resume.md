

# resume

Resumes the execution of the corresponding coroutine passing value as the return value of the last suspension point.

```kotlin
inline fun <T> Continuation<T>.resume(value: T)(source)
```

```kotlin
import kotlin.coroutines.*

fun main() {
    // Create a dummy Continuation that just prints the resumed value
    val continuation = object : Continuation<String> {
        override val context = EmptyCoroutineContext
        override fun resumeWith(result: Result<String>) {
            println("Resumed with: ${result.getOrThrow()}")
        }
    }

    // Resume the continuation, passing "Hello, Kotlin!" as the return value
    continuation.resume("Hello, Kotlin!")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/resume.html)

    