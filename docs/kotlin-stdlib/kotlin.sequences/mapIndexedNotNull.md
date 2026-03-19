

# mapIndexedNotNull

Returns a sequence containing only the non-null results of applying the given transform function to each element and its index in the original sequence.

```kotlin
fun <T, R : Any> Sequence<T>.mapIndexedNotNull(transform: (index: Int, T) -> R?): Sequence<R>(source)
```

```kotlin
val numbers = sequenceOf(10, 20, 30, 40, 50)

val result = numbers
    .mapIndexedNotNull { index, value ->
        // Keep only elements at even indices, convert them to strings
        if (index % 2 == 0) "Index $index: $value" else null
    }
    .toList()

println(result)   // Output: [Index 0: 10, Index 2: 30, Index 4: 50]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/map-indexed-not-null.html)

    