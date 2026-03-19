

# inv

Inverts the bits in this value.

```kotlin
inline fun Byte.inv(): Byte(source)
```

```kotlin
fun main() {
    val original: Byte = 0b0101_0010          // 0x52
    val inverted = original.inv()            // 0b1010_1101
    println("original: 0b${(original.toInt() and 0xFF).toString(2).padStart(8, '0')}")
    println("inverted: 0b${(inverted.toInt() and 0xFF).toString(2).padStart(8, '0')}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.experimental/inv.html)

    