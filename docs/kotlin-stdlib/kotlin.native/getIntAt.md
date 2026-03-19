

# getIntAt

Gets Int out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.getIntAt(index: Int): Int(source)
```

```kotlin
import kotlin.native.ExperimentalNativeApi

@OptIn(ExperimentalNativeApi::class)
fun main() {
    // Byte array containing the 4 bytes of an Int in little‑endian order
    val buffer = byteArrayOf(0x78, 0x56, 0x34, 0x12)

    // Read the Int starting at index 0
    val value = buffer.getIntAt(0)

    println(value)   // prints 305419896 (0x12345678)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-int-at.html)

    