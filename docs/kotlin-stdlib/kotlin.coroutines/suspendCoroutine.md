

# suspendCoroutine

Obtains the current continuation instance inside suspend functions and suspends the currently running coroutine.

```kotlin
inline suspend fun <T> suspendCoroutine(crossinline block: (Continuation<T>) -> Unit): T(source)
```

```kotlin
import kotlinx.coroutines.*
import kotlin.coroutines.*

fun asyncOperation(callback: (String) -> Unit) {
    Thread {
        Thread.sleep(1000)               // simulate asynchronous work
        callback("Result from async")
    }.start()
}

suspend fun getResult(): String = suspendCoroutine { cont ->
    asyncOperation { result ->
        cont.resume(result)             // resume the suspended coroutine with the result
    }
}

fun main() = runBlocking {
    val result = getResult()
    println(result)                     // prints: Result from async
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/suspend-coroutine.html)

    