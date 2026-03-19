

# AtomicArray

Creates a new AtomicArray if the given type with the given size, where each element is initialized by calling the given init function.

```kotlin
@ExperimentalAtomicApiinline fun <T> AtomicArray(size: Int, init: (Int) -> T): AtomicArray<T>(source)
```

```kotlin
import kotlin.concurrent.atomics.*
import kotlin.experimental.ExperimentalTypeInference

@ExperimentalAtomicApi
fun main() {
    // Create an AtomicArray of 5 Ints, each initialized to its index
    val array = AtomicArray(5) { it }

    // Read and print the initial values
    for (i in 0 until array.size) {
        println("array[$i] = ${array[i]}")
    }

    // Atomically set a new value at index 2
    array[2] = 42
    println("After setting, array[2] = ${array[2]}")

    // Atomically update a value using compareAndSet
    val success = array.compareAndSet(3, 3, 99)  // sets index 3 from 3 to 99
    println("compareAndSet succeeded: $success, array[3] = ${array[3]}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/-atomic-array.html)

    