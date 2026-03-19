

# emptyMap

Returns an empty read-only map of specified type.

```kotlin
fun <K, V> emptyMap(): Map<K, V>(source)
```

```kotlin
val empty: Map<String, Int> = emptyMap()

println(empty)          // Output: {}
println(empty.isEmpty()) // Output: true
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/empty-map.html)

    