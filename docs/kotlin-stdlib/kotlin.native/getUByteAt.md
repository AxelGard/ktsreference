

# getUByteAt

Gets UByte out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApifun ByteArray.getUByteAt(index: Int): UByte(source)
```

```kotlin
import kotlin.native.ExperimentalNativeApi

fun main() {
    val data = byteArrayOf(0x00, 0x7F, (-1).toByte())
    @OptIn(ExperimentalNativeApi::class)
    val value: UByte = data.getUByteAt(2)
    println(value)   // prints 255
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-u-byte-at.html)

    