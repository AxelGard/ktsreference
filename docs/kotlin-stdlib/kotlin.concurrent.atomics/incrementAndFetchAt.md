

# incrementAndFetchAt

Atomically increments the element of this AtomicIntArray at the given index by one and returns the new value of the element.

```kotlin
@ExperimentalAtomicApifun AtomicIntArray.incrementAndFetchAt(index: Int): Int(source)
```

```kotlin
import kotlin.concurrent.atoms.AtomicIntArray
import kotlin.concurrent.atoms.ExperimentalAtomicApi

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    // Create an AtomicIntArray with 5 elements, all initially 0
    val atomicArray = AtomicIntArray(5)

    // Atomically increment the element at index 2 by 1
    val newValue = atomicArray.incrementAndFetchAt(2)

    // Print the new value (should be 1)
    println("New value at index 2: $newValue")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/increment-and-fetch-at.html)

    