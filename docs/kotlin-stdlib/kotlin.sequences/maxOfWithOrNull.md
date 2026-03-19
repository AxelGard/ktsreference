

# maxOfWithOrNull

Returns the largest value according to the provided comparator among all values produced by selector function applied to each element in the sequence or null if the sequence is empty.

```kotlin
inline fun <T, R> Sequence<T>.maxOfWithOrNull(comparator: Comparator<in R>, selector: (T) -> R): R?(source)
```

```kotlin
val words = listOf("kotlin", "java", "csharp").asSequence()

// Find the longest word length in the sequence
val longestWordLength = words.maxOfWithOrNull(compareBy<Int> { it }) { it.length }

println(longestWordLength)   // prints: 6
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/max-of-with-or-null.html)

    