

# hexToUByte

Parses an UByte value from this string using the specified format.

```kotlin
inline fun String.hexToUByte(format: HexFormat = HexFormat.Default): UByte(source)
```

```kotlin
import kotlin.text.HexFormat

fun main() {
    val hexString = "FF"          // hexadecimal representation of 255
    val value: UByte = hexString.hexToUByte()   // parse to UByte
    println("Hex '$hexString' as UByte = $value") // prints: Hex 'FF' as UByte = 255
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/hex-to-u-byte.html)

    