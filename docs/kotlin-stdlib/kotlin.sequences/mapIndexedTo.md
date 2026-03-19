

# mapIndexedTo

Applies the given transform function to each element and its index in the original sequence and appends the results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, R, C : MutableCollection<in R>> Sequence<T>.mapIndexedTo(destination: C, transform: (index: Int, T) -> R): C(source)
```

```kotlin
val numbers = sequenceOf(10, 20, 30)

val result = mutableListOf<String>()
numbers.mapIndexedTo(result) { index, value ->
    "Item $index: $value"
}

println(result) // prints: [Item 0: 10, Item 1: 20, Item 2: 30]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/map-indexed-to.html)

    