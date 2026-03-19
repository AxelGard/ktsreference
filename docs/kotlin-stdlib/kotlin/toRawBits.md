

# toRawBits

Returns a bit representation of the specified floating-point value as Long according to the IEEE 754 floating-point "double format" bit layout, preserving NaN values exact layout.

```kotlin
expect fun Double.toRawBits(): Long(source)
```

```kotlin
fun main() {
    val number = 3.141592653589793
    val raw = number.toRawBits()
    println("Raw bits of $number: $raw")

    // Convert back to Double
    val backToDouble = raw.toDouble()
    println("Back to Double: $backToDouble")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/to-raw-bits.html)

    