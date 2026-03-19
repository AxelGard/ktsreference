

# filterIndexed

Returns a sequence containing only elements matching the given predicate.

```kotlin
fun <T> Sequence<T>.filterIndexed(predicate: (index: Int, T) -> Boolean): Sequence<T>(source)
```

```kotlin
val numbers = sequenceOf(10, 20, 30, 40, 50, 60)

val filtered = numbers.filterIndexed { index, _ ->
    // Keep elements whose index is even (0, 2, 4, ...)
    index % 2 == 0
}

println(filtered.toList())  // Output: [10, 30, 50]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/filter-indexed.html)

    