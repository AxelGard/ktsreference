

# associateWith

Returns a Map where keys are elements from the given sequence and values are produced by the valueSelector function applied to each element.

```kotlin
inline fun <K, V> Sequence<K>.associateWith(valueSelector: (K) -> V): Map<K, V>(source)
```

```kotlin
val fruits = sequenceOf("apple", "banana", "cherry")
val lengths = fruits.associateWith { it.length }
println(lengths)   // {apple=5, banana=6, cherry=6}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/associate-with.html)

    