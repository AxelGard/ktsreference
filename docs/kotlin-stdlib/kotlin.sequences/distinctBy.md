

# distinctBy

Returns a sequence containing only elements from the given sequence having distinct keys returned by the given selector function.

```kotlin
fun <T, K> Sequence<T>.distinctBy(selector: (T) -> K): Sequence<T>(source)
```

```kotlin
data class Person(val id: Int, val name: String)

val people = listOf(
    Person(1, "Alice"),
    Person(2, "Bob"),
    Person(3, "Alice"),
    Person(1, "Charlie")
)

val distinctNames = people
    .asSequence()
    .distinctBy { it.id }          // keep first Person for each unique id
    .toList()

println(distinctNames) // [Person(id=1, name=Alice), Person(id=2, name=Bob), Person(id=3, name=Alice)]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/distinct-by.html)

    