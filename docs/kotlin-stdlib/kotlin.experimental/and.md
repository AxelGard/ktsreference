

# and

Performs a bitwise AND operation between the two values.

```kotlin
infix inline fun Byte.and(other: Byte): Byte(source)
```

```kotlin
import kotlin.experimental.and

fun main() {
    val a: Byte = 0b1101_0110          // 214 in decimal
    val b: Byte = 0b1010_1100          // 172 in decimal
    val result: Byte = a and b        // 0b1000_0100 (132 in decimal)
    println("Result of a and b: $result")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.experimental/and.html)

    