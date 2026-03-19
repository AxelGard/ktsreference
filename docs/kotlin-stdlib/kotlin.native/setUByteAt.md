

# setUByteAt

Sets UByte out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.setUByteAt(index: Int, value: UByte)(source)
```

```kotlin
@OptIn(ExperimentalNativeApi::class)
fun main() {
    val buffer = ByteArray(4)

    buffer.setUByteAt(0, 0x01u)
    buffer.setUByteAt(1, 0x02u)
    buffer.setUByteAt(2, 0xFFu)
    buffer.setUByteAt(3, 0x00u)

    println(buffer.joinToString(" ") { "%02X".format(it) })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-u-byte-at.html)

    