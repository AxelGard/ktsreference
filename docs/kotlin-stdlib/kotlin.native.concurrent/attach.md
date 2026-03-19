

# attach

Error since 2.1

```kotlin
@ObsoleteWorkersApiinline fun <T> DetachedObjectGraph<T>.attach(): T(source)
```

```kotlin
import kotlin.native.concurrent.*

@OptIn(ObsoleteWorkersApi::class)
fun main() {
    // Original object living on the current worker (main thread)
    val numbers = listOf(1, 2, 3, 4, 5)

    // Detach the object graph – it can now be safely transferred to another worker
    val detached: DetachedObjectGraph<List<Int>> = detach(numbers)

    // Re‑attach the object graph back to the current worker (main thread)
    val reattached: List<Int> = detached.attach()

    // Use the reattached object as usual
    println("Numbers: $reattached")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native.concurrent/attach.html)

    