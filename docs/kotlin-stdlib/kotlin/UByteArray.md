

# UByteArray

Creates a new array of the specified size, where each element is calculated by calling the specified init function.

```kotlin
@ExperimentalUnsignedTypesinline fun UByteArray(size: Int, init: (Int) -> UByte): UByteArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    // Create an UByteArray of size 5 where each element is twice its index.
    val arr: UByteArray = UByteArray(5) { (it * 2).toUByte() }

    // Print the array contents
    println(arr.joinToString(prefix = "[", postfix = "]") { it.toString() })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-byte-array.html)

    