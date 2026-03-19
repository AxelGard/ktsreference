

# groupBy

Groups elements of the original sequence by the key returned by the given keySelector function applied to each element and returns a map where each group key is associated with a list of corresponding elements.

```kotlin
inline fun <T, K> Sequence<T>.groupBy(keySelector: (T) -> K): Map<K, List<T>>(source)
```

```kotlin
val words = sequenceOf("apple", "banana", "cherry", "date")
val groupedByLength = words.groupBy { it.length }
println(groupedByLength)   // Output: {5=[apple], 6=[banana, cherry], 4=[date]}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/group-by.html)

    