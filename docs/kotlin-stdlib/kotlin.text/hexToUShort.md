

# hexToUShort

Parses an UShort value from this string using the specified format.

```kotlin
inline fun String.hexToUShort(format: HexFormat = HexFormat.Default): UShort(source)
```

```kotlin
fun main() {
    val hexString = "1A2B"
    val value: UShort = hexString.hexToUShort()
    println("Parsed value: $value")   // Output: Parsed value: 6699
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/hex-to-u-short.html)

    