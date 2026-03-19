

# flatMap

Returns a single sequence of all elements from results of transform function being invoked on each element of original sequence.

```kotlin
@JvmName(name = "flatMapIterable")fun <T, R> Sequence<T>.flatMap(transform: (T) -> Iterable<R>): Sequence<R>(source)
```

```kotlin
val nested = listOf(
    listOf("a", "b"),
    listOf("c"),
    listOf("d", "e", "f")
)

val flat = nested.asSequence()
    .flatMap { it }          // flatMapIterable: (List<String>) -> Iterable<String>
    .toList()

println(flat)   // prints: [a, b, c, d, e, f]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/flat-map.html)

    