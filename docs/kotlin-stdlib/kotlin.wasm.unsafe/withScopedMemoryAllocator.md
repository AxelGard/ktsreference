

# withScopedMemoryAllocator

Runs the block of code, providing it a temporary MemoryAllocator as an argument, and returns the result of this block.

```kotlin
inline fun <T> withScopedMemoryAllocator(block: (allocator: MemoryAllocator) -> T): T(source)
```

```kotlin
import kotlin.wasm.unsafe.*

fun main() {
    val sum = withScopedMemoryAllocator { allocator ->
        // Allocate space for 5 integers
        val ptr = allocator.allocate<Int>(5)

        // Initialize the array
        for (i in 0 until 5) {
            ptr[i] = i + 1
        }

        // Compute the sum
        var total = 0
        for (i in 0 until 5) {
            total += ptr[i]
        }

        total   // value returned from the block
    }

    println("Sum: $sum")   // prints: Sum: 15
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.wasm.unsafe/with-scoped-memory-allocator.html)

    