

# toString

Returns a string representation of this Byte value in the specified radix.

```kotlin
fun UByte.toString(radix: Int): String(source)
```

```kotlin
fun main() {
    val value: UByte = 255u

    println("Decimal: ${value.toString(10)}") // 255
    println("Hex: ${value.toString(16)}")    // ff
    println("Binary: ${value.toString(2)}")  // 11111111
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-string.html)

    