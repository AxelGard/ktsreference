

# asKotlinAtomicArray

Casts the given java.util.concurrent.atomic.AtomicIntegerArray instance to AtomicIntArray.

```kotlin
@ExperimentalAtomicApifun AtomicIntegerArray.asKotlinAtomicArray(): AtomicIntArray(source)
```

```kotlin
import kotlin.concurrent.atomics.*

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    // Create a Java AtomicIntegerArray
    val javaArray = java.util.concurrent.atomic.AtomicIntegerArray(3).apply {
        set(0, 1)
        set(1, 2)
        set(2, 3)
    }

    // Cast it to Kotlin's AtomicIntArray
    val kotlinArray = javaArray.asKotlinAtomicArray()

    // Read values
    println(kotlinArray[0]) // 1
    println(kotlinArray[1]) // 2
    println(kotlinArray[2]) // 3

    // Atomically update
    kotlinArray[0] = 10
    println(kotlinArray[0]) // 10

    // Atomic get-and-increment
    val old = kotlinArray.getAndIncrement(1)
    println(old)            // 2
    println(kotlinArray[1]) // 3

    // Atomic add-and-get
    val sum = kotlinArray.addAndGet(2, 5)
    println(sum)            // 8
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/as-kotlin-atomic-array.html)

    