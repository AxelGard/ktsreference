

# hexToInt

Parses an Int value from this string using the specified format.

```kotlin
fun String.hexToInt(format: HexFormat = HexFormat.Default): Int(source)
```

```kotlin
import kotlin.text.hexToInt

fun main() {
    val hexString = "1A3F"
    val intValue = hexString.hexToInt()  // converts hex to decimal Int
    println("Hex $hexString as Int is $intValue")  // prints: Hex 1A3F as Int is 6719
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/hex-to-int.html)

    