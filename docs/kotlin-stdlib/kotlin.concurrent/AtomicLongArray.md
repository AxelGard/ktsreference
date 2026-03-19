

# AtomicLongArray

Creates a new AtomicLongArray of the given size, where each element is initialized by calling the given init function.

```kotlin
@ExperimentalStdlibApiinline fun AtomicLongArray(size: Int, init: (Int) -> Long): AtomicLongArray(source)
```

```kotlin
import kotlin.concurrent.AtomicLongArray
import kotlin.experimental.ExperimentalStdlibApi

@OptIn(ExperimentalStdlibApi::class)
fun main() {
    // Create an AtomicLongArray of size 5, initialized with index * 10
    val array = AtomicLongArray(5) { it.toLong() * 10 }

    // Read an element
    println(array[2])   // 20

    // Write an element
    array[2] = 42
    println(array[2])   // 42

    // Compare-and-set
    val success = array.compareAndSet(2, 42, 100)
    println(success)    // true
    println(array[2])   // 100
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent/-atomic-long-array.html)

    