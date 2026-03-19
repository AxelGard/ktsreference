

# associateWithTo

Populates and returns the destination mutable map with key-value pairs for each element of the given sequence, where key is the element itself and value is provided by the valueSelector function applied to that key.

```kotlin
@IgnorableReturnValueinline fun <K, V, M : MutableMap<in K, in V>> Sequence<K>.associateWithTo(destination: M, valueSelector: (K) -> V): M(source)
```

```kotlin
val fruits = sequenceOf("apple", "banana", "cherry")
val lengths = mutableMapOf<String, Int>()

fruits.associateWithTo(lengths) { it.length }

println(lengths)  // Output: {apple=5, banana=6, cherry=6}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/associate-with-to.html)

    