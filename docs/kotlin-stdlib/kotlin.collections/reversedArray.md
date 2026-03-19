

# reversedArray

Returns an array with elements of this array in reversed order.

```kotlin
fun <T> Array<T>.reversedArray(): Array<T>(source)
```

fun main() {
    val original = arrayOf(1, 2, 3, 4, 5)
    val reversed = original.reversedArray()
    println("Original: ${original.joinToString()}")
    println("Reversed: ${reversed.joinToString()}")
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reversed-array.html)

    