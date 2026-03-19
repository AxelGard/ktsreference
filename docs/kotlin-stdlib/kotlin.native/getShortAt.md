

# getShortAt

Gets Short out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.getShortAt(index: Int): Short(source)
```

```kotlin
import kotlin.experimental.ExperimentalNativeApi

@OptIn(ExperimentalNativeApi::class)
fun main() {
    // A byte array containing four bytes
    val bytes = byteArrayOf(0x01, 0x02, 0x03, 0x04)

    // Read a Short value starting at index 0 (bytes 0x01 and 0x02)
    val firstShort: Short = bytes.getShortAt(0)   // 258

    // Read a Short value starting at index 2 (bytes 0x03 and 0x04)
    val secondShort: Short = bytes.getShortAt(2) // 772

    println("firstShort = $firstShort, secondShort = $secondShort")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-short-at.html)

    