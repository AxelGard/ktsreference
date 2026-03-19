

# setUIntAt

Sets UInt out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.setUIntAt(index: Int, value: UInt)(source)
```

```kotlin
import kotlin.native.*

@OptIn(ExperimentalNativeApi::class)
fun main() {
    // Create a byte buffer of 8 bytes
    val buffer = ByteArray(8)

    // Write an UInt value (0x12345678) at byte index 0
    buffer.setUIntAt(0, 0x12345678u)

    // Print the buffer contents in hexadecimal
    println(buffer.joinToString(prefix = "[", postfix = "]") {
        it.toUByte().toString(16).padStart(2, '0')
    })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-u-int-at.html)

    