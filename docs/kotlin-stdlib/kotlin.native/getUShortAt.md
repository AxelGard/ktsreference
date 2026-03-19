

# getUShortAt

Gets UShort out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApi@ExperimentalUnsignedTypesexternal fun ByteArray.getUShortAt(index: Int): UShort(source)
```

```kotlin
import kotlin.experimental.*

@OptIn(ExperimentalNativeApi::class, ExperimentalUnsignedTypes::class)
fun main() {
    // A simple byte buffer containing four bytes
    val buffer = byteArrayOf(0x01, 0x02, 0x03, 0x04)

    // Read a UShort (2 bytes) starting at index 0
    val value: UShort = buffer.getUShortAt(0)

    // Print the unsigned short value
    println("UShort at index 0: $value")   // → UShort at index 0: 513
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-u-short-at.html)

    