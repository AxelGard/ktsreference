

# hexToShort

Parses a Short value from this string using the specified format.

```kotlin
fun String.hexToShort(format: HexFormat = HexFormat.Default): Short(source)
```

```kotlin
import kotlin.text.HexFormat

fun main() {
    val hexString = "0x1A2B"
    val shortValue: Short = hexString.hexToShort()          // Uses default format
    // or specify a format explicitly
    val shortWithCustom = hexString.hexToShort(HexFormat.Default)
    println(shortValue)           // 6699
    println(shortWithCustom)      // 6699
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/hex-to-short.html)

    