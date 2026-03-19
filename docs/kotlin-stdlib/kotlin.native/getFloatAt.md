

# getFloatAt

Gets Float out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.getFloatAt(index: Int): Float(source)
```

```kotlin
import kotlin.native.ExperimentalNativeApi
import kotlin.native.getFloatAt

@ExperimentalNativeApi
fun main() {
    // ByteArray with the little‑endian IEEE‑754 bytes for 1.0f
    val bytes = byteArrayOf(0x00, 0x00, 0x80.toByte(), 0x3f.toByte())

    val value: Float = bytes.getFloatAt(0)
    println(value)   // prints: 1.0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-float-at.html)

    