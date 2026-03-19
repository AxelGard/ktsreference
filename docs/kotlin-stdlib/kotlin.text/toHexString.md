

# toHexString

Formats bytes in this array using the specified format.

```kotlin
fun ByteArray.toHexString(format: HexFormat = HexFormat.Default): String(source)
```

```kotlin
import kotlin.text.HexFormat

fun main() {
    // Sample byte array
    val bytes = byteArrayOf(0x01, 0x23, 0x45, 0x67, 0x89, 0xAB.toByte(), 0xCD.toByte(), 0xEF.toByte())

    // Default formatting (no delimiter, lowercase hex)
    val hexDefault = bytes.toHexString()
    println("Default: $hexDefault")          // prints: 0123456789abcdef

    // Custom formatting: uppercase with colon delimiter
    val hexCustom = bytes.toHexString(
        HexFormat.ofDelimiter(":")
            .withUpperCase()
    )
    println("Custom: $hexCustom")            // prints: 01:23:45:67:89:AB:CD:EF
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-hex-string.html)

    