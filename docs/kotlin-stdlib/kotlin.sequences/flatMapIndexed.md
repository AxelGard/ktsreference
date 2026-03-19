

# flatMapIndexed

Returns a single sequence of all elements yielded from results of transform function being invoked on each element and its index in the original sequence.

```kotlin
@JvmName(name = "flatMapIndexedIterable")fun <T, R> Sequence<T>.flatMapIndexed(transform: (index: Int, T) -> Iterable<R>): Sequence<R>(source)
```

```kotlin
val words = sequenceOf("apple", "banana", "cherry")

val result = words.flatMapIndexed { index, word ->
    listOf(
        "$word (index $index)",
        "$word reversed: ${word.reversed()}"
    )
}

result.forEach { println(it) }
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/flat-map-indexed.html)

    