

# maxByOrNull

Returns the first element yielding the largest value of the given selector function or null if there are no elements.

```kotlin
inline fun <T, R : Comparable<R>> Sequence<T>.maxByOrNull(selector: (T) -> R): T?(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = sequenceOf(
    Person("Alice", 28),
    Person("Bob", 34),
    Person("Charlie", 22)
)

val oldest = people.maxByOrNull { it.age }
println(oldest?.name)   // prints: Bob
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/max-by-or-null.html)

    