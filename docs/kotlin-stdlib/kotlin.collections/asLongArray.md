

# asLongArray

Returns an array of type LongArray, which is a view of this array where each element is a signed reinterpretation of the corresponding element of this array.

```kotlin
@ExperimentalUnsignedTypesinline fun ULongArray.asLongArray(): LongArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val uLongs: ULongArray = uLongArrayOf(10uL, 20uL, 30uL)
    val longs: LongArray = uLongs.asLongArray()
    println(longs.joinToString()) // prints: 10, 20, 30
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-long-array.html)

    