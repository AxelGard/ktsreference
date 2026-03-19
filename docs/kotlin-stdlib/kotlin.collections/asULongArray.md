

# asULongArray

Returns an array of type ULongArray, which is a view of this array where each element is an unsigned reinterpretation of the corresponding element of this array.

```kotlin
@ExperimentalUnsignedTypesinline fun LongArray.asULongArray(): ULongArray(source)
```

```kotlin
import kotlin.experimental.*

@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val longArray = longArrayOf(-1L, 0L, 1L, 42L)
    val uLongArray: ULongArray = longArray.asULongArray()

    println("Original LongArray: ${longArray.joinToString()}")
    println("Reinterpreted ULongArray: ${uLongArray.joinToString()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-u-long-array.html)

    