

# flatten

Returns a sequence of all elements from all sequences in this sequence.

```kotlin
fun <T> Sequence<Sequence<T>>.flatten(): Sequence<T>(source)
```

```kotlin
val nested = sequenceOf(
    sequenceOf("a", "b"),
    sequenceOf("c"),
    sequenceOf("d", "e", "f")
)

val flattened: Sequence<String> = nested.flatten()

println(flattened.toList())  // prints: [a, b, c, d, e, f]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/flatten.html)

    