

# stringMapOf

Constructs the specialized implementation of HashMap with String keys, which stores the keys as properties of JS object without hashing them.

```kotlin
fun <V> stringMapOf(vararg pairs: Pair<String, V>): HashMap<String, V>(source)
```

```kotlin
val map = stringMapOf(
    "name" to "Alice",
    "age" to 30,
    "city" to "New York"
)

println(map["name"]) // Alice
println(map["age"])  // 30
println(map["city"]) // New York
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/string-map-of.html)

    