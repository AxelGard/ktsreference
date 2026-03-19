

# getLongAt

Gets Long out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.getLongAt(index: Int): Long(source)
```

```kotlin
import kotlin.native.ExperimentalNativeApi

@OptIn(ExperimentalNativeApi::class)
fun main() {
    // A byte array that contains the long value 1L in little‑endian order.
    val bytes = byteArrayOf(
        0x01, 0x00, 0x00, 0x00,  // lower 4 bytes
        0x00, 0x00, 0x00, 0x00   // upper 4 bytes
    )

    // Read the long value starting at index 0.
    val value = bytes.getLongAt(0)

    println("Read long value: $value")  // prints: Read long value: 1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-long-at.html)

    