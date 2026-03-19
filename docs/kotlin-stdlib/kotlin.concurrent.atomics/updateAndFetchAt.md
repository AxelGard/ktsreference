

# updateAndFetchAt

Atomically updates the element of this AtomicIntArray at the given index using the transform function and returns the updated value of the element.

```kotlin
@ExperimentalAtomicApiexpect inline fun AtomicIntArray.updateAndFetchAt(index: Int, transform: (Int) -> Int): Int(source)
```

```kotlin
import kotlin.concurrent.atomics.*

@ExperimentalAtomicApi
fun main() {
    val array = AtomicIntArray(5)

    // Initialize the array with values 0, 1, 2, 3, 4
    for (i in 0 until array.size) {
        array[i] = i
    }

    // Atomically update the element at index 2, adding 1 to its current value
    val updated = array.updateAndFetchAt(2) { it + 1 }

    println("Updated value at index 2: $updated")
    println("Array contents: ${Array(array.size) { array[it] }}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/update-and-fetch-at.html)

    