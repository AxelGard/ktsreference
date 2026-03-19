

# asByteArray

Returns an array of type ByteArray, which is a view of this array where each element is a signed reinterpretation of the corresponding element of this array.

```kotlin
@ExperimentalUnsignedTypesinline fun UByteArray.asByteArray(): ByteArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun demoAsByteArray() {
    val uBytes: UByteArray = ubyteArrayOf(0u, 1u, 255u, 128u)
    val bytes: ByteArray = uBytes.asByteArray()

    // Print the signed byte values
    println(bytes.contentToString())   // Output: [0, 1, -1, -128]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-byte-array.html)

    