

# sortedArrayDescending

Returns an array with all elements of this array sorted descending according to their natural sort order.

```kotlin
fun <T : Comparable<T>> Array<T>.sortedArrayDescending(): Array<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(3, 1, 4, 1, 5, 9, 2, 6)
    val sortedDescending = numbers.sortedArrayDescending()
    println(sortedDescending.joinToString())
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sorted-array-descending.html)

    