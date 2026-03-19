

# maxWith

Returns the first element having the largest value according to the provided comparator.

```kotlin
@JvmName(name = "maxWithOrThrow")fun <T> Sequence<T>.maxWith(comparator: Comparator<in T>): T(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = sequenceOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val oldest = people.maxWith(compareBy<Person> { it.age })
println("Oldest person: $oldest")  // Output: Oldest person: Person(name=Charlie, age=35)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/max-with.html)

    