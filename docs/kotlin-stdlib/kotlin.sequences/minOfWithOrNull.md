

# minOfWithOrNull

Returns the smallest value according to the provided comparator among all values produced by selector function applied to each element in the sequence or null if the sequence is empty.

```kotlin
inline fun <T, R> Sequence<T>.minOfWithOrNull(comparator: Comparator<in R>, selector: (T) -> R): R?(source)
```

```kotlin
data class Person(val name: String)

val people = sequenceOf(
    Person("Alice"),
    Person("Bob"),
    Person("Charlie")
)

val shortestNameLength = people.minOfWithOrNull(Comparator.naturalOrder<Int>()) { it.name.length }
println(shortestNameLength)   // prints 3
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/min-of-with-or-null.html)

    