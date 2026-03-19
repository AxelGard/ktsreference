

# coroutineContext

Returns the context of the current coroutine.

```kotlin
val coroutineContext: CoroutineContext(source)
```

```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    // Launch a child coroutine with a custom name
    launch(CoroutineName("MyChild")) {
        // Print the entire coroutine context of this coroutine
        println("Coroutine context: $coroutineContext")

        // Access a specific element from the context
        val name = coroutineContext[CoroutineName]?.name
        println("Coroutine name: $name")

        // Access the Job element
        val job = coroutineContext[Job]
        println("Is job active? ${job?.isActive}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/coroutine-context.html)

    