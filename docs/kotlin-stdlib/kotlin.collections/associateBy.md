

# associateBy

Returns a Map containing the elements from the given array indexed by the key returned from keySelector function applied to each element.

```kotlin
inline fun <T, K> Array<out T>.associateBy(keySelector: (T) -> K): Map<K, T>(source)
```

```kotlin
data class Person(val id: Int, val name: String)

val people = arrayOf(
    Person(1, "Alice"),
    Person(2, "Bob"),
    Person(3, "Charlie")
)

val peopleById: Map<Int, Person> = people.associateBy { it.id }

println(peopleById[2]?.name)  // Prints: Bob
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/associate-by.html)

    