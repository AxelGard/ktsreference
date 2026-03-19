

# minWith

Returns the first element having the smallest value according to the provided comparator.

```kotlin
@JvmName(name = "minWithOrThrow")fun <T> Sequence<T>.minWith(comparator: Comparator<in T>): T(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = sequenceOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val youngest = people.minWith(compareBy<Person> { it.age })
println("Youngest: ${youngest.name}, age ${youngest.age}")
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/min-with.html)

    