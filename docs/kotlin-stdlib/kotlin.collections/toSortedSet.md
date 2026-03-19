

# toSortedSet

Returns a new SortedSet of all elements.

```kotlin
fun <T : Comparable<T>> Array<out T>.toSortedSet(): SortedSet<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(10, 3, 5, 2, 8)
    val sortedSet: SortedSet<Int> = numbers.toSortedSet()
    println(sortedSet)  // Output: [2, 3, 5, 8, 10]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-sorted-set.html)

    