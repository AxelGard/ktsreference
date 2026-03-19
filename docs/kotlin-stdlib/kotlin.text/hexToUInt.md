

# hexToUInt

Parses an UInt value from this string using the specified format.

```kotlin
inline fun String.hexToUInt(format: HexFormat = HexFormat.Default): UInt(source)
```

```kotlin
import kotlin.text.hexToUInt

fun main() {
    val hexString = "FF"          // hexadecimal representation
    val decimalValue: UInt = hexString.hexToUInt()   // parses to UInt
    println("Hex $hexString is UInt $decimalValue") // prints: Hex FF is UInt 255
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/hex-to-u-int.html)

    