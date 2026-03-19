

# minWithOrNull

Returns the first element having the smallest value according to the provided comparator or null if there are no elements.

```kotlin
fun <T> Sequence<T>.minWithOrNull(comparator: Comparator<in T>): T?(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = sequenceOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val youngest = people.minWithOrNull(compareBy<Person> { it.age })
println(youngest?.name)   // Output: Bob
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/min-with-or-null.html)

    