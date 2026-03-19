

# getULongAt

Gets ULong out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApi@ExperimentalUnsignedTypesexternal fun ByteArray.getULongAt(index: Int): ULong(source)
```

```kotlin
import kotlin.native.concurrent.ExperimentalNativeApi
import kotlin.experimental.ExperimentalUnsignedTypes

@OptIn(ExperimentalNativeApi::class, ExperimentalUnsignedTypes::class)
fun main() {
    // A byte array containing 16 bytes (two ULong values).
    val buffer = byteArrayOf(
        0x01, 0x02, 0x03, 0x04,
        0x05, 0x06, 0x07, 0x08,   // first ULong (little‑endian)
        0x09, 0x0A, 0x0B, 0x0C,
        0x0D, 0x0E, 0x0F, 0x10    // second ULong (little‑endian)
    )

    // Read the first ULong starting at index 0.
    val firstULong: ULong = buffer.getULongAt(0)
    println("First ULong: $firstULong")

    // Read the second ULong starting at index 8.
    val secondULong: ULong = buffer.getULongAt(8)
    println("Second ULong: $secondULong")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-u-long-at.html)

    