

# copyInto

Copies this array or its subrange into the destination array and returns that array.

```kotlin
@IgnorableReturnValue@ExperimentalUnsignedTypesinline fun UIntArray.copyInto(destination: UIntArray, destinationOffset: Int = 0, startIndex: Int = 0, endIndex: Int = size): UIntArray(source)
```

```kotlin
fun main() {
    // Source array with 5 elements
    val src = uintArrayOf(10u, 20u, 30u, 40u, 50u)

    // Destination array with 8 elements (initially all zeros)
    val dest = UIntArray(8)

    // Copy a subrange (20u, 30u, 40u) into dest starting at index 3
    src.copyInto(
        destination = dest,
        destinationOffset = 3, // start writing at index 3 of dest
        startIndex = 1,        // start at element 1 of src (20u)
        endIndex = 4           // end before element 4 of src (exclusive)
    )

    println(dest.joinToString()) // Output: 0, 0, 0, 20, 30, 40, 0, 0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/copy-into.html)

    