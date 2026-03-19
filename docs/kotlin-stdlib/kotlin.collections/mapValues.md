

# mapValues

Returns a new map with entries having the keys of this map and the values obtained by applying the transform function to each entry in this Map.

```kotlin
inline fun <K, V, R> Map<out K, V>.mapValues(transform: (Map.Entry<K, V>) -> R): Map<K, R>(source)
```

```kotlin
val original = mapOf("a" to 1, "b" to 2, "c" to 3)

val doubled = original.mapValues { (_, value) -> value * 2 }

println(doubled) // prints {a=2, b=4, c=6}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-values.html)

    