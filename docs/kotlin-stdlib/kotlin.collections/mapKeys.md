

# mapKeys

Returns a new Map with entries having the keys obtained by applying the transform function to each entry in this Map and the values of this map.

```kotlin
inline fun <K, V, R> Map<out K, V>.mapKeys(transform: (Map.Entry<K, V>) -> R): Map<R, V>(source)
```

```kotlin
fun main() {
    val original = mapOf("Apple" to 3, "Banana" to 5, "Cherry" to 2)

    // Convert all keys to lower case
    val lowerCaseKeys = original.mapKeys { entry -> entry.key.lowercase() }

    println(lowerCaseKeys)   // {apple=3, banana=5, cherry=2}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-keys.html)

    