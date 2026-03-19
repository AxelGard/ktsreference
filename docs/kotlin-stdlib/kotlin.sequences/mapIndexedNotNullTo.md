

# mapIndexedNotNullTo

Applies the given transform function to each element and its index in the original sequence and appends only the non-null results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, R : Any, C : MutableCollection<in R>> Sequence<T>.mapIndexedNotNullTo(destination: C, transform: (index: Int, T) -> R?): C(source)
```

```kotlin
val numbers = sequenceOf("zero", "one", "two", "three", "four")
val result = mutableListOf<String>()

numbers.mapIndexedNotNullTo(result) { index, word ->
    if (index % 2 == 0) word.uppercase() else null
}

println(result) // [ZERO, TWO, FOUR]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/map-indexed-not-null-to.html)

    