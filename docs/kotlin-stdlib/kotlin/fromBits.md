

# fromBits

Returns the Double value corresponding to a given bit representation.

```kotlin
expect fun Double.Companion.fromBits(bits: Long): Double(source)
```

```kotlin
fun main() {
    // IEEE‑754 bit pattern for the double value 1.0
    val bits: Long = 0x3FF0000000000000L

    // Convert the bit pattern back to a Double
    val value: Double = Double.fromBits(bits)

    println("Bit pattern 0x${bits.toString(16)} corresponds to Double value: $value")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/from-bits.html)

    