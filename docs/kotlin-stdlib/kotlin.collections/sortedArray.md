

# sortedArray

Returns an array with all elements of this array sorted according to their natural sort order.

```kotlin
fun <T : Comparable<T>> Array<T>.sortedArray(): Array<T>(source)
```

```kotlin
val unsorted = arrayOf(3, 1, 4, 1, 5)
val sorted = unsorted.sortedArray()
println(sorted.contentToString())  // prints [1, 1, 3, 4, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sorted-array.html)

    