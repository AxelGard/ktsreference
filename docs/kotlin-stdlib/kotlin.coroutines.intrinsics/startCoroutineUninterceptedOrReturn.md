

# startCoroutineUninterceptedOrReturn

Starts an unintercepted coroutine without a receiver and with result type T and executes it until its first suspension. Returns the result of the coroutine or throws its exception if it does not suspend or COROUTINE_SUSPENDED if it suspends. In the latter case, the completion continuation is invoked when the coroutine completes with a result or an exception.

```kotlin
expect inline fun <T> suspend () -> T.startCoroutineUninterceptedOrReturn(completion: Continuation<T>): Any?(source)
```

```kotlin
import kotlin.coroutines.*
import kotlin.coroutines.intrinsics.startCoroutineUninterceptedOrReturn
import kotlin.coroutines.intrinsics.COROUTINE_SUSPENDED
import kotlin.coroutines.suspendCoroutine

fun main() {
    // A suspend lambda that suspends once and then returns a value
    val block = suspend {
        println("Before suspend")
        suspendCoroutine<Unit> { cont ->
            println("Suspending now")
            cont.resume(Unit)          // resume after suspension
        }
        println("After suspend")
        42                            // result of the suspend block
    }

    // Continuation that will receive the final result
    val completion = object : Continuation<Int> {
        override val context = EmptyCoroutineContext
        override fun resumeWith(result: Result<Int>) {
            println("Continuation resumed with ${result.getOrNull()}")
        }
    }

    // Start the coroutine unintercepted and check its return value
    val res = block.startCoroutineUninterceptedOrReturn(completion)
    if (res == COROUTINE_SUSPENDED) {
        println("Coroutine suspended; completion will be called later")
    } else {
        println("Coroutine finished immediately with $res")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines.intrinsics/start-coroutine-unintercepted-or-return.html)

    