

# takeLowestOneBit

Returns a number having a single bit set in the position of the least significant set bit of this Byte number, or zero, if this number is zero.

```kotlin
inline fun Byte.takeLowestOneBit(): Byte(source)
```

```kotlin
fun main() {
    val byte: Byte = 0b1010.toByte()  // binary: 00001010
    val lowest = byte.takeLowestOneBit()
    println("Lowest set bit: $lowest") // prints 2
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/take-lowest-one-bit.html)

    