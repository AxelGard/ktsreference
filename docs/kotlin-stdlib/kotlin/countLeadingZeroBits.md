

# countLeadingZeroBits

Counts the number of consecutive most significant bits that are zero in the binary representation of this Byte number.

```kotlin
inline fun Byte.countLeadingZeroBits(): Int(source)
```

```kotlin
fun main() {
    val b: Byte = 0b00010010   // binary representation of 18
    val leadingZeros = b.countLeadingZeroBits()
    println("Number of leading zero bits in $b: $leadingZeros")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/count-leading-zero-bits.html)

    