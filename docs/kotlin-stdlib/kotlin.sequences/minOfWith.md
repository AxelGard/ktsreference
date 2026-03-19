

# minOfWith

Returns the smallest value according to the provided comparator among all values produced by selector function applied to each element in the sequence.

```kotlin
inline fun <T, R> Sequence<T>.minOfWith(comparator: Comparator<in R>, selector: (T) -> R): R(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = sequenceOf(
    Person("Alice", 30),
    Person("Bob", 20),
    Person("Charlie", 25)
)

val youngestAge = people.minOfWith(Comparator.naturalOrder<Int>(), { it.age })
println(youngestAge)   // prints 20
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/min-of-with.html)

    