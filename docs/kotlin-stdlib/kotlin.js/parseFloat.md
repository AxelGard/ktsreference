

# parseFloat

Use toDouble() instead.

```kotlin
external fun parseFloat(s: String, radix: Int = definedExternally): Double(source)
```

```kotlin
fun main() {
    val str = "123.45"
    val num = parseFloat(str)          // 123.45
    println("Parsed value: $num")

    // Using radix (base) for integer parsing
    val hex = "1A"
    val hexValue = parseFloat(hex, 16) // 26.0
    println("Hex value: $hexValue")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/parse-float.html)

    