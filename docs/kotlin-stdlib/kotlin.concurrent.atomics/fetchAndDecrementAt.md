

# fetchAndDecrementAt

Atomically decrements the element of this AtomicIntArray at the given index by one and returns the old value of the element.

```kotlin
@ExperimentalAtomicApifun AtomicIntArray.fetchAndDecrementAt(index: Int): Int(source)
```

```kotlin
import kotlin.concurrent.atomics.*

@OptIn(ExperimentalAtomicApifun::class)
fun main() {
    // Create an AtomicIntArray with 3 elements
    val array = AtomicIntArray(3)

    // Initialise the first element to 5
    array.set(0, 5)

    // Atomically decrement the first element and get its old value
    val oldValue = array.fetchAndDecrementAt(0)

    println("Old value: $oldValue")          // prints 5
    println("New value: ${array[0]}")        // prints 4
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/fetch-and-decrement-at.html)

    