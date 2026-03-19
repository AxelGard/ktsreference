

# asJavaAtomicArray

Casts the given AtomicIntArray instance to java.util.concurrent.atomic.AtomicIntegerArray.

```kotlin
@ExperimentalAtomicApifun AtomicIntArray.asJavaAtomicArray(): AtomicIntegerArray(source)
```

```kotlin
import kotlin.concurrent.atomic.*
import java.util.concurrent.atomic.AtomicIntegerArray

@OptIn(ExperimentalAtomicApifun::class)
fun main() {
    // Create a Kotlin AtomicIntArray
    val kotlinArray = atomicIntArrayOf(1, 2, 3, 4, 5)

    // Convert it to a Java AtomicIntegerArray
    val javaArray: AtomicIntegerArray = kotlinArray.asJavaAtomicArray()

    // Modify the array using Java's API
    javaArray.set(0, 10)
    javaArray.incrementAndGet(1)

    // Read the modified values back through Kotlin's API
    for (i in kotlinArray.indices) {
        println("index $i: ${kotlinArray[i]}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/as-java-atomic-array.html)

    