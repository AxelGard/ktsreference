

# linkedMapOf

Returns an empty new LinkedHashMap.

```kotlin
inline fun <K, V> linkedMapOf(): LinkedHashMap<K, V>(source)
```

```kotlin
val map = linkedMapOf<String, Int>()

map["apple"] = 3
map["banana"] = 5
map["cherry"] = 2

for ((fruit, quantity) in map) {
    println("$fruit: $quantity")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/linked-map-of.html)

    