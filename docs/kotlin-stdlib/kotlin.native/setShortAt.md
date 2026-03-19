

# setShortAt

Sets Short out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.setShortAt(index: Int, value: Short)(source)
```

```kotlin
import kotlin.native.concurrent.ExperimentalNativeApi

@OptIn(ExperimentalNativeApi::class)
fun main() {
    val buffer = ByteArray(4)

    // Store the short value 0x1234 at index 0
    buffer.setShortAt(0, 0x1234.toShort())

    // Store the short value 0xABCD at index 2
    buffer.setShortAt(2, 0xABCD.toShort())

    // Print the byte array contents in hex
    println(buffer.joinToString(prefix = "[", postfix = "]") { "%02X".format(it) })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-short-at.html)

    