

# buildMap

Builds a new read-only Map by populating a MutableMap using the given builderAction and returning a read-only map with the same key-value pairs.

```kotlin
inline fun <K, V> buildMap(builderAction: MutableMap<K, V>.() -> Unit): Map<K, V>(source)
```

val fruitColors = buildMap<String, String> {
    put("apple", "red")
    put("banana", "yellow")
    put("grape", "purple")
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/build-map.html)

    