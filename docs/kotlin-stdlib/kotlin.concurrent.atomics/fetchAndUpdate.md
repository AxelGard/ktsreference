

# fetchAndUpdate

Atomically updates the value of this AtomicInt with the value obtained by calling the transform function on the current value and returns the value replaced by the updated one.

```kotlin
@ExperimentalAtomicApiexpect inline fun AtomicInt.fetchAndUpdate(transform: (Int) -> Int): Int(source)
```

```kotlin
import kotlin.concurrent.atomic.*
import kotlin.ExperimentalAtomicApi

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    val counter = AtomicInt(0)
    val previous = counter.fetchAndUpdate { it + 1 }

    println("Previous value: $previous")
    println("New value: ${counter.value}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/fetch-and-update.html)

    