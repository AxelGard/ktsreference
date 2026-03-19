

# mapIndexed

Returns a sequence containing the results of applying the given transform function to each element and its index in the original sequence.

```kotlin
fun <T, R> Sequence<T>.mapIndexed(transform: (index: Int, T) -> R): Sequence<R>(source)
```

```kotlin
val numbers = sequenceOf(10, 20, 30, 40)

val indexedStrings = numbers
    .mapIndexed { index, number -> "Item #$index is $number" }
    .toList()

println(indexedStrings)
// Output: [Item #0 is 10, Item #1 is 20, Item #2 is 30, Item #3 is 40]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/map-indexed.html)

    