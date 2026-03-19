

# asUByteArray

Returns an array of type UByteArray, which is a view of this array where each element is an unsigned reinterpretation of the corresponding element of this array.

```kotlin
@ExperimentalUnsignedTypesinline fun ByteArray.asUByteArray(): UByteArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    // Create a signed byte array with some sample values
    val signedBytes = byteArrayOf(0x01, 0x02, 0xFF.toByte())

    // Reinterpret the byte array as an unsigned byte array
    val unsignedBytes: UByteArray = signedBytes.asUByteArray()

    // Print the unsigned values
    println(unsignedBytes.joinToString(", ") { it.toString() })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-u-byte-array.html)

    