

# atomicArrayOfNulls

Returns a new AtomicArray of the given type with the given size, initialized with null values.

```kotlin
@ExperimentalAtomicApiinline fun <T> atomicArrayOfNulls(size: Int): AtomicArray<T?>(source)
```

```kotlin
import kotlin.concurrent.atomics.*

@OptIn(ExperimentalAtomicApi::class)
fun main() {
    // Create an AtomicArray of size 5, all entries initialized to null
    val arr = atomicArrayOfNulls<Int>(5)

    // Verify initial state (all nulls)
    println("initial: ${arr[0]}, ${arr[1]}, ${arr[2]}, ${arr[3]}, ${arr[4]}")

    // Set the element at index 2 to 10
    arr[2] = 10
    println("after set: ${arr[2]}")

    // Compare and set: replace 10 with 20 only if current value is 10
    val replaced = arr.compareAndSet(2, 10, 20)
    println("compareAndSet result: $replaced, new value: ${arr[2]}")

    // Attempt to replace 10 with 30 (should fail because current value is 20)
    val failed = arr.compareAndSet(2, 10, 30)
    println("compareAndSet failed: $failed, value remains: ${arr[2]}")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.concurrent.atomics/atomic-array-of-nulls.html)

    