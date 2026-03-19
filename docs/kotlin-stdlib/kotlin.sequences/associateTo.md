

# associateTo

Populates and returns the destination mutable map with key-value pairs provided by transform function applied to each element of the given sequence.

```kotlin
@IgnorableReturnValueinline fun <T, K, V, M : MutableMap<in K, in V>> Sequence<T>.associateTo(destination: M, transform: (T) -> Pair<K, V>): M(source)
```

```kotlin
val fruits = sequenceOf("apple", "banana", "cherry")

val fruitLengths = mutableMapOf<String, Int>()
fruits.associateTo(fruitLengths) { fruit -> fruit to fruit.length }

// fruitLengths is now: { apple=5, banana=6, cherry=6 }
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/associate-to.html)

    