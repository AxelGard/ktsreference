

# setCharAt

Sets Char out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.setCharAt(index: Int, value: Char)(source)
```

```kotlin
import kotlin.native.experimental.ExperimentalNativeApi

@ExperimentalNativeApi
fun main() {
    val buffer = ByteArray(10) { 0 }   // create a 10‑byte buffer
    buffer.setCharAt(0, 'H')           // store 'H' at position 0
    buffer.setCharAt(2, 'i')           // store 'i' at position 2

    // Print the buffer contents as a string (UTF‑8 decoding)
    println(buffer.decodeToString())
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-char-at.html)

    