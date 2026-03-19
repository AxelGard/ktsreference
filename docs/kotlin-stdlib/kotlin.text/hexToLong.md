

# hexToLong

Parses a Long value from this string using the specified format.

```kotlin
fun String.hexToLong(format: HexFormat = HexFormat.Default): Long(source)
```

```kotlin
import kotlin.text.HexFormat

fun main() {
    val hexString = "1A3F"
    val number: Long = hexString.hexToLong()          // uses HexFormat.Default
    println("Hex $hexString as Long: $number")        // prints: Hex 1A3F as Long: 6719

    // With a custom format (e.g., uppercase and 4 digits)
    val customNumber = hexString.hexToLong(
        HexFormat { it.letterCase = HexFormat.LetterCase.UPPER; it.minimumWidth = 4 }
    )
    println("Custom format: $customNumber")            // prints: Custom format: 6719
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/hex-to-long.html)

    