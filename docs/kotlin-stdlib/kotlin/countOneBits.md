

# countOneBits

Counts the number of set bits in the binary representation of this Byte number.

```kotlin
inline fun Byte.countOneBits(): Int(source)
```

```kotlin
fun main() {
    val byte: Byte = 0b10101010.toByte()
    val setBits = byte.countOneBits()
    println("Byte 0b10101010 has $setBits set bits.")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/count-one-bits.html)

    