

# mapKeysTo

Populates the given destination map with entries having the keys obtained by applying the transform function to each entry in this Map and the values of this map.

```kotlin
@IgnorableReturnValueinline fun <K, V, R, M : MutableMap<in R, in V>> Map<out K, V>.mapKeysTo(destination: M, transform: (Map.Entry<K, V>) -> R): M(source)
```

```kotlin
val original = mapOf(1 to "one", 2 to "two", 3 to "three")

val destination = mutableMapOf<String, String>()
original.mapKeysTo(destination) { it.key.toString() }

println(destination) // Output: {1=one, 2=two, 3=three}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-keys-to.html)

    