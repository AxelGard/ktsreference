

# toByteArray

Warning since 1.9

```kotlin
external fun ImmutableBlob.toByteArray(startIndex: Int = 0, endIndex: Int = size): ByteArray(source)
```

```kotlin
import kotlinx.cinterop.*   // If needed for Kotlin/Native
import kotlin.native.*      // Import ImmutableBlob

fun main() {
    // Original data
    val original = byteArrayOf(0x48, 0x65, 0x6C, 0x6C, 0x6F) // "Hello"

    // Create an ImmutableBlob from the byte array
    val blob = ImmutableBlob(original)

    // Convert the entire blob back to a byte array
    val fullBytes = blob.toByteArray()               // uses default startIndex = 0, endIndex = size

    // Convert a subrange of the blob to a byte array (bytes 1..3)
    val subBytes = blob.toByteArray(startIndex = 1, endIndex = 4)

    println("Full bytes: ${fullBytes.joinToString(prefix = "[", postfix = "]")}")
    println("Sub bytes: ${subBytes.joinToString(prefix = "[", postfix = "]")}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/to-byte-array.html)

    