

# getCharAt

Gets Char out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.getCharAt(index: Int): Char(source)
```

```kotlin
import kotlin.experimental.ExperimentalNativeApi
import kotlin.native.concurrent.*

@OptIn(ExperimentalNativeApi::class)
fun main() {
    // A byte array containing ASCII codes for 'K', 'o', 't', 'l', 'i', 'n'
    val bytes = byteArrayOf(75, 111, 116, 108, 105, 110)

    // Get the character at index 2 ('t')
    val charAtIndex2: Char = bytes.getCharAt(2)

    println("ByteArray: ${bytes.joinToString()}")   // 75, 111, 116, 108, 105, 110
    println("Character at index 2: $charAtIndex2") // t
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/get-char-at.html)

    