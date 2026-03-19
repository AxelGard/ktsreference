

# UIntArray

Creates a new array of the specified size, where each element is calculated by calling the specified init function.

```kotlin
@ExperimentalUnsignedTypesinline fun UIntArray(size: Int, init: (Int) -> UInt): UIntArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    // Create a UIntArray of size 5 where each element is the index value cast to UInt
    val unsignedArray = UIntArray(5) { index -> index.toUInt() }

    // Print the array contents
    unsignedArray.forEach { println(it) }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-int-array.html)

    