

# fetchAndIncrementAt

Atomically increments the element of this AtomicIntArray at the given index by one and returns the old value of the element.

```kotlin
@ExperimentalAtomicApifun AtomicIntArray.fetchAndIncrementAt(index: Int): Int(source)
```

```kotlin
import kotlin.concurrent.atomics.*

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    val array = AtomicIntArray(5)
    array[0] = 10

    // Atomically increment the element at index 0 and get its old value
    val oldValue = array.fetchAndIncrementAt(0)
    println("Old value at index 0: $oldValue")   // prints: 10
    println("New value at index 0: ${array[0]}") // prints: 11
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/fetch-and-increment-at.html)

    