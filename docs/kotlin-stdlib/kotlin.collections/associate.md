

# associate

Returns a Map containing key-value pairs provided by transform function applied to elements of the given array.

```kotlin
inline fun <T, K, V> Array<out T>.associate(transform: (T) -> Pair<K, V>): Map<K, V>(source)
```

```kotlin
data class User(val id: Int, val name: String)

val users = arrayOf(
    User(1, "Alice"),
    User(2, "Bob"),
    User(3, "Charlie")
)

val idToName: Map<Int, String> = users.associate { user ->
    user.id to user.name
}

println(idToName)   // {1=Alice, 2=Bob, 3=Charlie}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/associate.html)

    