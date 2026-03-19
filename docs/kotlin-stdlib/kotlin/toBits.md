

# toBits

Returns a bit representation of the specified floating-point value as Long according to the IEEE 754 floating-point "double format" bit layout.

```kotlin
expect fun Double.toBits(): Long(source)
```

```kotlin
fun main() {
    val value: Double = 3.1415
    val bits: Long = value.toBits()
    println("Double value: $value")
    println("Bit representation: 0x${bits.toString(16)}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/to-bits.html)

    