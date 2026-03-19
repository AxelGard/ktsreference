

# sum

Returns the sum of all elements in the sequence.

```kotlin
@JvmName(name = "sumOfByte")fun Sequence<Byte>.sum(): Int(source)
```

```kotlin
fun main() {
    // Create a sequence of Byte values
    val byteSequence: Sequence<Byte> = sequenceOf(10.toByte(), 20.toByte(), 30.toByte())

    // Sum the bytes (result is an Int)
    val totalSum: Int = byteSequence.sum()

    println("Sum of bytes: $totalSum")  // Output: Sum of bytes: 60
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sum.html)

    