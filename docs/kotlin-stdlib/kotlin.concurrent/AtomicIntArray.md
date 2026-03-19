

# AtomicIntArray

Creates a new AtomicIntArray of the given size, where each element is initialized by calling the given init function.

```kotlin
@ExperimentalStdlibApiinline fun AtomicIntArray(size: Int, init: (Int) -> Int): AtomicIntArray(source)
```

```kotlin
import kotlin.concurrent.AtomicIntArray

// Create an AtomicIntArray of size 5, where each element is initialized to its index multiplied by 2
val atomicArray = AtomicIntArray(5) { index -> index * 2 }

// Read and print each value
for (i in 0 until atomicArray.size) {
    println("Element $i: ${atomicArray[i]}")
}

// Atomically add 10 to the element at index 2
atomicArray.addAndGet(2, 10)
println("After add, element 2: ${atomicArray[2]}")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/-atomic-int-array.html)

    