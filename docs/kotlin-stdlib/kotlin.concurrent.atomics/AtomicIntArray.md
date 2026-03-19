

# AtomicIntArray

Creates a new AtomicIntArray of the given size, where each element is initialized by calling the given init function.

```kotlin
@ExperimentalAtomicApiinline fun AtomicIntArray(size: Int, init: (Int) -> Int): AtomicIntArray(source)
```

```kotlin
import kotlin.concurrent.atomics.*

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    // Create an AtomicIntArray of size 5, initializing each element with its index
    val atomicArray = AtomicIntArray(5) { index -> index }

    // Read elements atomically
    println("Initial values:")
    for (i in 0 until atomicArray.size) {
        println("index $i = ${atomicArray[i]}")
    }

    // Atomically set a value
    atomicArray[2] = 42
    println("\nAfter setting index 2 to 42: ${atomicArray[2]}")

    // Atomically add to a value
    atomicArray.addAndGet(4, 10)
    println("After adding 10 to index 4: ${atomicArray[4]}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/-atomic-int-array.html)

    