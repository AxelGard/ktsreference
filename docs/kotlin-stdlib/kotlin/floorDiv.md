

# floorDiv

Divides this value by the other value, flooring the result to an integer that is closer to negative infinity.

```kotlin
inline fun Byte.floorDiv(other: Byte): Int(source)
```

```kotlin
fun main() {
    val a: Byte = 10
    val b: Byte = 3
    val result = a.floorDiv(b)          // result is 3
    println("$a floorDiv $b = $result")  // prints: 10 floorDiv 3 = 3
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/floor-div.html)

    