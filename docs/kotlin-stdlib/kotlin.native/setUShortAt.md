

# setUShortAt

Sets UShort out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApi@ExperimentalUnsignedTypesexternal fun ByteArray.setUShortAt(index: Int, value: UShort)(source)
```

```kotlin
import kotlin.native.concurrent.ExperimentalNativeApi
import kotlin.experimental.ExperimentalUnsignedTypes

@OptIn(ExperimentalNativeApi::class, ExperimentalUnsignedTypes::class)
fun main() {
    // Create a byte buffer of 4 bytes
    val buffer = ByteArray(4)

    // Write the UShort value 0xABCD at index 0 (writes bytes at positions 0 and 1)
    buffer.setUShortAt(0, 0xABCDu)

    // The remaining bytes are untouched
    println(buffer.joinToString(separator = " ") { "0x%02X".format(it) })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-u-short-at.html)

    