

# hexToUByteArray

Parses a byte array from this string using the specified format.

```kotlin
@ExperimentalUnsignedTypesinline fun String.hexToUByteArray(format: HexFormat = HexFormat.Default): UByteArray(source)
```

```kotlin
import kotlin.text.hexToUByteArray

@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val hex = "deadbeef"
    val bytes: UByteArray = hex.hexToUByteArray()
    println(bytes.joinToString(" ") { it.toString(16).padStart(2, '0') })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/hex-to-u-byte-array.html)

    