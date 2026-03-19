

# decrementAndFetchAt

Atomically decrements the element of this AtomicIntArray at the given index by one and returns the new value of the element.

```kotlin
@ExperimentalAtomicApifun AtomicIntArray.decrementAndFetchAt(index: Int): Int(source)
```

```kotlin
import kotlin.concurrent.atomics.AtomicIntArray
import kotlin.experimental.ExperimentalAtomicApifun

@OptIn(ExperimentalAtomicApifun::class)
fun main() {
    // Create an AtomicIntArray with 5 elements: 0, 10, 20, 30, 40
    val array = AtomicIntArray(5) { index -> index * 10 }

    // Atomically decrement the element at index 2 (which is 20) by 1
    val newValue = array.decrementAndFetchAt(2)

    println("New value at index 2: $newValue")   // → 19
    println("Array contents: ${array.joinToString()}") // → 0, 10, 19, 30, 40
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/decrement-and-fetch-at.html)

    