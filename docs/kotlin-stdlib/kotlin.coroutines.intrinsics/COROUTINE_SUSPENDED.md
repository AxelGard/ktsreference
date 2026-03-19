

# COROUTINE_SUSPENDED

This value is used as a return value of suspendCoroutineUninterceptedOrReturn block argument to state that the execution was suspended and will not return any result immediately.

```kotlin
val COROUTINE_SUSPENDED: Any(source)
```

```kotlin
import kotlin.coroutines.*
import kotlin.coroutines.intrinsics.*
import kotlinx.coroutines.runBlocking

// Simulate an asynchronous callback-based API
fun asyncOperation(callback: (String) -> Unit) {
    Thread {
        Thread.sleep(500)          // pretend work is done after 0.5 seconds
        callback("Result")
    }.start()
}

// Suspend function that bridges the callback API with coroutines
suspend fun fetchResult(): String =
    suspendCoroutineUninterceptedOrReturn { cont ->
        asyncOperation { result ->
            cont.resume(result)
        }
        COROUTINE_SUSPENDED   // indicate that the coroutine is suspended
    }

fun main() = runBlocking {
    val value = fetchResult()
    println("Fetched: $value")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines.intrinsics/-c-o-r-o-u-t-i-n-e_-s-u-s-p-e-n-d-e-d.html)

    