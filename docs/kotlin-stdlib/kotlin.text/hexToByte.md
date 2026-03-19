

# hexToByte

Parses a Byte value from this string using the specified format.

```kotlin
fun String.hexToByte(format: HexFormat = HexFormat.Default): Byte(source)
```

```kotlin
import kotlin.text.HexFormat

fun main() {
    val hexString = "1A"          // a two‑digit hex representation
    val byteValue: Byte = hexString.hexToByte()  // default format (HexFormat.Default)

    println("Hex string '$hexString' as byte: $byteValue")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/hex-to-byte.html)

    