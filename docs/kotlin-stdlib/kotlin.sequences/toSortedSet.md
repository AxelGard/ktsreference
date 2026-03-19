

# toSortedSet

Returns a new SortedSet of all elements.

```kotlin
fun <T : Comparable<T>> Sequence<T>.toSortedSet(): SortedSet<T>(source)
```

```kotlin
val words = sequenceOf("banana", "apple", "cherry", "date", "apple")
val sortedSet = words.toSortedSet()
println(sortedSet)   // Output: [apple, banana, cherry, date]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/to-sorted-set.html)

    