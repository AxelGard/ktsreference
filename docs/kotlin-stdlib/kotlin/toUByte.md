

# toUByte

Converts this Byte value to UByte.

```kotlin
inline fun Byte.toUByte(): UByte(source)
```

```kotlin
fun main() {
    val signedPositive: Byte = 42
    val signedNegative: Byte = -1

    val unsignedPositive: UByte = signedPositive.toUByte()
    val unsignedNegative: UByte = signedNegative.toUByte()

    println("Positive: $signedPositive -> $unsignedPositive")
    println("Negative: $signedNegative -> $unsignedNegative")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/to-u-byte.html)

    