

# associate

Returns a Map containing key-value pairs provided by transform function applied to elements of the given sequence.

```kotlin
inline fun <T, K, V> Sequence<T>.associate(transform: (T) -> Pair<K, V>): Map<K, V>(source)
```

val words = sequenceOf("apple", "banana", "cherry")
val map = words.associate { it to it.length }

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/associate.html)

    