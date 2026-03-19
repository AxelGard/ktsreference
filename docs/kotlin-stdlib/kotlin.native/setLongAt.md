

# setLongAt

Sets Long out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.setLongAt(index: Int, value: Long)(source)
```

```kotlin
import kotlin.native.*
import kotlin.native.ExperimentalNativeApi

@OptIn(ExperimentalNativeApi::class)
fun main() {
    // Create a buffer large enough to hold one Long (8 bytes)
    val buffer = ByteArray(8)

    // Store a 64‑bit value at the beginning of the buffer
    buffer.setLongAt(0, 0x1122334455667788L)

    // Optional: read back the value to verify it was written correctly
    val readValue = buffer.getLongAt(0)
    println("Value stored in buffer: 0x${readValue.toString(16)}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-long-at.html)

    