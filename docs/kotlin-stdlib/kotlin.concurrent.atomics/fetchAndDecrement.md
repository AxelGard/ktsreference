

# fetchAndDecrement

Atomically decrements the current value of this AtomicInt by one and returns the old value.

```kotlin
@ExperimentalAtomicApifun AtomicInt.fetchAndDecrement(): Int(source)
```

```kotlin
import kotlinx.atomicfu.atomicInt
import kotlinx.atomicfu.ExperimentalAtomicApi

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    val counter = atomicInt(5)
    println("Initial value: ${counter.value}")           // 5

    val old = counter.fetchAndDecrement()                // old value: 5
    println("fetchAndDecrement returned: $old")

    println("New value after decrement: ${counter.value}") // 4
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/fetch-and-decrement.html)

    