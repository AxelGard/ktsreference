

# xor

Performs a bitwise XOR operation between the two values.

```kotlin
infix inline fun Byte.xor(other: Byte): Byte(source)
```

```kotlin
import kotlin.experimental.xor

fun main() {
    val byte1: Byte = 0b1010_1100.toByte()
    val byte2: Byte = 0b1100_1010.toByte()

    val result: Byte = byte1 xor byte2

    println("Result: ${result.toInt().toString(2).padStart(8, '0')}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.experimental/xor.html)

    