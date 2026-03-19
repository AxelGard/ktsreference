

# associateBy

Returns a Map containing the elements from the given sequence indexed by the key returned from keySelector function applied to each element.

```kotlin
inline fun <T, K> Sequence<T>.associateBy(keySelector: (T) -> K): Map<K, T>(source)
```

```kotlin
data class User(val username: String, val age: Int)

val users = sequenceOf(
    User("alice", 30),
    User("bob", 25),
    User("charlie", 35)
)

val usersByName: Map<String, User> = users.associateBy { it.username }

println(usersByName["bob"])   // Prints: User(username=bob, age=25)
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/associate-by.html)

    