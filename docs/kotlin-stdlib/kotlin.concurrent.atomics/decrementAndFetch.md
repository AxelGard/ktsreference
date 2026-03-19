

# decrementAndFetch

Atomically decrements the current value of this AtomicInt by one and returns the new value.

```kotlin
@ExperimentalAtomicApifun AtomicInt.decrementAndFetch(): Int(source)
```

```kotlin
import kotlin.concurrent.atomics.*
import kotlin.ExperimentalAtomicApi

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    val counter = atomic(5)
    println("Initial value: ${counter.value}")   // 5
    val newValue = counter.decrementAndFetch()
    println("After decrementAndFetch: $newValue") // 4
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/decrement-and-fetch.html)

    