

# updateAt

Atomically updates the element of this AtomicIntArray at the given index using the transform function.

```kotlin
@ExperimentalAtomicApiexpect inline fun AtomicIntArray.updateAt(index: Int, transform: (Int) -> Int)(source)
```

```kotlin
import kotlin.concurrent.atomics.*

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    // Create an AtomicIntArray with initial values
    val array = atomicIntArrayOf(10, 20, 30)

    // Atomically update the element at index 1 (second element)
    array.updateAt(1) { currentValue ->
        // For example, double the current value
        currentValue * 2
    }

    // Verify the update
    println(array[1])  // prints 40
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/update-at.html)

    