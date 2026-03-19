

# firstNotNullOf

Returns the first non-null value produced by transform function being applied to elements of this sequence in iteration order, or throws NoSuchElementException if no non-null value was produced.

```kotlin
inline fun <T, R : Any> Sequence<T>.firstNotNullOf(transform: (T) -> R?): R(source)
```

```kotlin
data class User(val name: String, val email: String?)

val users = sequenceOf(
    User("alice", null),
    User("bob", "bob@example.com"),
    User("carol", null)
)

val firstEmail = users.firstNotNullOf { it.email }

println(firstEmail)   // → bob@example.com
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/first-not-null-of.html)

    