

# fetchAndIncrement

Atomically increments the current value of this AtomicInt by one and returns the old value.

```kotlin
@ExperimentalAtomicApifun AtomicInt.fetchAndIncrement(): Int(source)
```

import kotlin.concurrent.atomics.AtomicInt
import kotlin.concurrent.atomics.newAtomicInt
import kotlin.experimental.ExperimentalAtomicApi

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    val counter = newAtomicInt(0)
    repeat(5) {
        val old = counter.fetchAndIncrement()
        println("Old value: $old, New value: ${counter.value}")
    }
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/fetch-and-increment.html)

    