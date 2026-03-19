

# AtomicArray

Creates a new AtomicArray of the given size, where each element is initialized by calling the given init function.

```kotlin
@ExperimentalStdlibApiinline fun <T> AtomicArray(size: Int, init: (Int) -> T): AtomicArray<T>(source)
```

```kotlin
import kotlin.concurrent.AtomicArray
import kotlin.concurrent.AtomicArrayElement

@OptIn(ExperimentalStdlibApi::class)
fun main() {
    // Create an AtomicArray of size 5 where each element is twice its index
    val array = AtomicArray(5) { index -> index * 2 }

    // Read all elements
    array.forEachIndexed { i, value ->
        println("array[$i] = $value")
    }

    // Update element at index 3
    array[3] = 42

    // Read the updated element
    println("After update, array[3] = ${array[3]}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/-atomic-array.html)

    