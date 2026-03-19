

# HexFormat

Builds a new HexFormat by configuring its format options using the specified builderAction, and returns the resulting format.

```kotlin
inline fun HexFormat(builderAction: HexFormat.Builder.() -> Unit): HexFormat(source)
```

```kotlin
import kotlin.text.HexFormat

fun main() {
    // Create a HexFormat instance with custom settings using the inline builder
    val formatter = HexFormat {
        withSeparator('-')          // add '-' between each byte
        withPrefix("0x")            // prepend "0x" to the output
        withPadding('0', 4)         // pad each byte to 4 characters with '0'
    }

    // Example byte array
    val bytes = byteArrayOf(0x1A, 0x2B, 0x3C)

    // Convert the byte array to a formatted hex string
    val hexString = formatter.formatHex(bytes)
    println(hexString)  // prints: 0x1A-2B-3C

    // Parse the hex string back into a byte array
    val parsedBytes = formatter.parseHex(hexString)
    println(parsedBytes.contentToString())  // prints: [26, 43, 60]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/-hex-format.html)

    