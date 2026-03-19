

# hexToByteArray

Parses a byte array from this string using the specified format.

```kotlin
fun String.hexToByteArray(format: HexFormat = HexFormat.Default): ByteArray(source)
```

```kotlin
import kotlin.text.hexToByteArray

fun main() {
    val hexString = "48656c6c6f2c20576f726c6421"   // "Hello, World!"
    val byteArray: ByteArray = hexString.hexToByteArray()
    println(byteArray.toHexString()) // prints: 48 65 6c 6c 6f 2c 20 57 6f 72 6c 64 21
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/hex-to-byte-array.html)

    