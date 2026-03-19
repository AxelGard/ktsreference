

# countTrailingZeroBits

Counts the number of consecutive least significant bits that are zero in the binary representation of this Byte number.

```kotlin
inline fun Byte.countTrailingZeroBits(): Int(source)
```

```kotlin
fun main() {
    val byte1: Byte = 8          // 00001000
    val byte2: Byte = 24         // 00011000
    val byte3: Byte = 0          // 00000000

    println("${byte1} has ${byte1.countTrailingZeroBits()} trailing zero bit(s)")
    println("${byte2} has ${byte2.countTrailingZeroBits()} trailing zero bit(s)")
    println("${byte3} has ${byte3.countTrailingZeroBits()} trailing zero bit(s)")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/count-trailing-zero-bits.html)

    