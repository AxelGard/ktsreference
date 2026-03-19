

# mutableMapOf

Returns an empty new MutableMap.

```kotlin
inline fun <K, V> mutableMapOf(): MutableMap<K, V>(source)
```

```kotlin
val map = mutableMapOf<String, Int>()

// Add entries
map["apple"] = 3
map["banana"] = 5

// Access a value
println(map["apple"])      // 3

// Remove an entry
map.remove("banana")

// Iterate over entries
for ((fruit, count) in map) {
    println("$fruit: $count")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/mutable-map-of.html)

    