

# takeHighestOneBit

Returns a number having a single bit set in the position of the most significant set bit of this Byte number, or zero, if this number is zero.

```kotlin
inline fun Byte.takeHighestOneBit(): Byte(source)
```

```kotlin
fun main() {
    val byte: Byte = 0b01101000.toByte()   // 104 in decimal
    val highestOneBit: Byte = byte.takeHighestOneBit()
    println("Original: $byte, Highest one bit: $highestOneBit")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/take-highest-one-bit.html)

    