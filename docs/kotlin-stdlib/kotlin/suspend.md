

# suspend

A functional type builder that ensures the given block has a suspend modifier and can be used as a suspend function.

```kotlin
inline fun <R> suspend(noinline block: suspend () -> R): suspend () -> R(source)
```

```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    // Create a suspend function using the `suspend` builder
    val loadData: suspend () -> String = suspend {
        delay(1000)          // Simulate some async work
        "Data loaded!"
    }

    // Invoke the suspend function inside a coroutine
    println(loadData())     // Prints: Data loaded!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/suspend.html)

    