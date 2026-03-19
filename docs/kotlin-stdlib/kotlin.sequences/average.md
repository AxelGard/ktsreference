

# average

Returns an average value of elements in the sequence.

```kotlin
@JvmName(name = "averageOfByte")fun Sequence<Byte>.average(): Double(source)
```

```kotlin
fun main() {
    val byteSeq = sequenceOf(10.toByte(), 20.toByte(), 30.toByte())
    println("Average: ${byteSeq.average()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/average.html)

    