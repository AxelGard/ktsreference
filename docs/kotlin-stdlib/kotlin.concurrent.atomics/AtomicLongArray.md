

# AtomicLongArray

Creates a new AtomicLongArray of the given size, where each element is initialized by calling the given init function.

```kotlin
@ExperimentalAtomicApiinline fun AtomicLongArray(size: Int, init: (Int) -> Long): AtomicLongArray(source)
```

```kotlin
import kotlin.concurrent.atomics.AtomicLongArray
import kotlin.concurrent.atomics.ExperimentalAtomicApi

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    // Create an AtomicLongArray of size 5, initializing each element with its index value
    val array = AtomicLongArray(5) { index -> index.toLong() }

    // Read and print the current values
    for (i in 0 until array.size()) {
        println("array[$i] = ${array[i]}")
    }

    // Atomically add 10 to each element
    for (i in 0 until array.size()) {
        array.addAndGet(i, 10L)
    }

    // Print the updated values
    for (i in 0 until array.size()) {
        println("array[$i] after add = ${array[i]}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/-atomic-long-array.html)

    