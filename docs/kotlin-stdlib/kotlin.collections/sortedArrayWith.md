

# sortedArrayWith

Returns an array with all elements of this array sorted according the specified comparator.

```kotlin
fun <T> Array<out T>.sortedArrayWith(comparator: Comparator<in T>): Array<out T>(source)
```

```kotlin
val words = arrayOf("banana", "apple", "cherry")

val sorted = words.sortedArrayWith(
    Comparator { a, b -> a.length.compareTo(b.length) }
)

println(sorted.joinToString())
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sorted-array-with.html)

    