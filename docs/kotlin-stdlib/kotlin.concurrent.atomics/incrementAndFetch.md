

# incrementAndFetch

Atomically increments the current value of this AtomicInt by one and returns the new value.

```kotlin
@ExperimentalAtomicApifun AtomicInt.incrementAndFetch(): Int(source)
```

```kotlin
import kotlin.concurrent.atomics.AtomicInt
import kotlin.concurrent.atomics.experimental.ExperimentalAtomicApi

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    val counter = AtomicInt(0)
    println("Initial value: ${counter.value}")   // 0

    val newValue = counter.incrementAndFetch()
    println("After increment: $newValue")         // 1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/increment-and-fetch.html)

    