

# sliceArray

Returns an array containing elements of this array at specified indices.

```kotlin
fun <T> Array<T>.sliceArray(indices: Collection<Int>): Array<T>(source)
```

```kotlin
fun main() {
    val original = arrayOf(1, 2, 3, 4, 5)
    val indices = listOf(0, 2, 4) // pick first, third, and fifth elements

    val sliced = original.sliceArray(indices)

    println(sliced.joinToString()) // prints: 1, 3, 5
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/slice-array.html)

    