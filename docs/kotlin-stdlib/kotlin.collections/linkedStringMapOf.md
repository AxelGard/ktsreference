

# linkedStringMapOf

Constructs the specialized implementation of LinkedHashMap with String keys, which stores the keys as properties of JS object without hashing them.

```kotlin
fun <V> linkedStringMapOf(vararg pairs: Pair<String, V>): LinkedHashMap<String, V>(source)
```

```kotlin
val users = linkedStringMapOf(
    "alice" to 28,
    "bob"   to 34,
    "carol" to 22
)

println(users["alice"]) // 28
println(users.keys)     // [alice, bob, carol]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/linked-string-map-of.html)

    