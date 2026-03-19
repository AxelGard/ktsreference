

# toUByteArray

Warning since 1.9

```kotlin
@ExperimentalUnsignedTypesexternal fun ImmutableBlob.toUByteArray(startIndex: Int = 0, endIndex: Int = size): UByteArray(source)
```

```kotlin
import kotlin.native.ImmutableBlob
import kotlin.experimental.ExperimentalUnsignedTypes

@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    // Original byte data
    val data = byteArrayOf(0x0A, 0x1B, 0x2C, 0x3D)

    // Create an ImmutableBlob from the byte array
    val blob = ImmutableBlob(data)

    // Convert the entire blob to a UByteArray
    val allBytes: UByteArray = blob.toUByteArray()

    // Convert a slice (bytes at indices 1 and 2) to a UByteArray
    val partBytes: UByteArray = blob.toUByteArray(startIndex = 1, endIndex = 3)

    println("All bytes: ${allBytes.joinToString(", ") { it.toString() }}")
    println("Part bytes: ${partBytes.joinToString(", ") { it.toString() }}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/to-u-byte-array.html)

    