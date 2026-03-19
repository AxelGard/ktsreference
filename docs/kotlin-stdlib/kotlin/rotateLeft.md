

# rotateLeft

Rotates the binary representation of this Byte number left by the specified bitCount number of bits. The most significant bits pushed out from the left side reenter the number as the least significant bits on the right side.

```kotlin
fun Byte.rotateLeft(bitCount: Int): Byte(source)
```

```kotlin
fun main() {
    val original: Byte = 0b01010110          // 0x56
    val rotated = original.rotateLeft(3)     // rotate left by 3 bits

    println("Original: 0x${original.toUByte().toString(16).padStart(2, '0')}")
    println("Rotated : 0x${rotated.toUByte().toString(16).padStart(2, '0')}")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/rotate-left.html)

    