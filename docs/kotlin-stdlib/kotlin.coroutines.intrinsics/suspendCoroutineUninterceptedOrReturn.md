

# suspendCoroutineUninterceptedOrReturn

Obtains the current continuation instance inside suspend functions and either suspends currently running coroutine or returns result immediately without suspension.

```kotlin
inline suspend fun <T> suspendCoroutineUninterceptedOrReturn(crossinline block: (Continuation<T>) -> Any?): T(source)
```

```kotlin
import kotlinx.coroutines.*
import kotlin.coroutines.intrinsics.*

suspend fun fetchValue(immediate: Boolean): Int =
    suspendCoroutineUninterceptedOrReturn { cont ->
        if (immediate) {
            // Return immediately without suspending
            42
        } else {
            // Suspend and resume later
            GlobalScope.launch {
                delay(1_000)
                cont.resume(84)
            }
            COROUTINE_SUSPENDED
        }
    }

fun main() = runBlocking {
    println("immediate: ${fetchValue(true)}")   // prints 42
    println("delayed:   ${fetchValue(false)}")  // prints 84 after 1 second
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines.intrinsics/suspend-coroutine-unintercepted-or-return.html)

    