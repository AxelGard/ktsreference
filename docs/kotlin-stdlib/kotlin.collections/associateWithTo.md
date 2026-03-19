

# associateWithTo

Populates and returns the destination mutable map with key-value pairs for each element of the given array, where key is the element itself and value is provided by the valueSelector function applied to that key.

```kotlin
@IgnorableReturnValueinline fun <K, V, M : MutableMap<in K, in V>> Array<out K>.associateWithTo(destination: M, valueSelector: (K) -> V): M(source)
```

```kotlin
val names = arrayOf("Alice", "Bob", "Charlie")
val map = mutableMapOf<String, Int>()

// Populate `map` with each name as key and its length as value
names.associateWithTo(map) { it.length }

println(map) // {Alice=5, Bob=3, Charlie=7}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/associate-with-to.html)

    