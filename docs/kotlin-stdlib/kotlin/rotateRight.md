

# rotateRight

Rotates the binary representation of this Byte number right by the specified bitCount number of bits. The least significant bits pushed out from the right side reenter the number as the most significant bits on the left side.

```kotlin
fun Byte.rotateRight(bitCount: Int): Byte(source)
```

```kotlin
fun main() {
    val original: Byte = 0b0101_0110          // 86 in decimal
    val rotated = original.rotateRight(2)    // shift right by 2 bits

    println("Original: ${original.toInt() and 0xFF}".padStart(8, '0'))
    println("Rotated : ${rotated.toInt() and 0xFF}".padStart(8, '0'))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/rotate-right.html)

    