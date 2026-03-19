

# maxWithOrNull

Returns the first element having the largest value according to the provided comparator or null if there are no elements.

```kotlin
fun <T> Sequence<T>.maxWithOrNull(comparator: Comparator<in T>): T?(source)
```

```kotlin
val fruits = listOf("apple", "banana", "cherry")

val longestFruit = fruits.asSequence()
    .maxWithOrNull(compareBy<String> { it.length })

println(longestFruit)   // Output: banana
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/max-with-or-null.html)

    