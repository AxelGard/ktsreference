

# getOrSet

Gets the value in the current thread's copy of this thread-local variable or replaces the value with the result of calling default function in case if that value was null.

```kotlin
inline fun <T : Any> ThreadLocal<T>.getOrSet(default: () -> T): T(source)
```

```kotlin
import java.util.concurrent.Executors

// Thread-local variable that holds an integer value
val threadLocalValue = ThreadLocal<Int>()

fun main() {
    // Create a pool with two threads
    val executor = Executors.newFixedThreadPool(2)

    // Submit two tasks that each use getOrSet to initialize the thread-local value
    repeat(2) { index ->
        executor.submit {
            // If the value is not set in this thread, initialize it to (index + 1) * 10
            val value = threadLocalValue.getOrSet { (index + 1) * 10 }
            println("Thread ${Thread.currentThread().name} has value $value")
        }
    }

    executor.shutdown()
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/get-or-set.html)

    