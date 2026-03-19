

# containsKey

Returns true if the map contains the specified key.

```kotlin
inline fun <K> Map<out K, *>.containsKey(key: K): Boolean(source)
```

```kotlin
val map = mapOf("a" to 1, "b" to 2)

println(map.containsKey("a")) // true
println(map.containsKey("c")) // false
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/contains-key.html)

    