

# hexToULong

Parses an ULong value from this string using the specified format.

```kotlin
inline fun String.hexToULong(format: HexFormat = HexFormat.Default): ULong(source)
```

```kotlin
fun main() {
    val hexString = "1A3F"
    val uLongValue: ULong = hexString.hexToULong()
    println("Hex '$hexString' as ULong: $uLongValue")  // Output: Hex '1A3F' as ULong: 6719
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/hex-to-u-long.html)

    