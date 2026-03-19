

# minByOrNull

Returns the first element yielding the smallest value of the given selector function or null if there are no elements.

```kotlin
inline fun <T, R : Comparable<R>> Sequence<T>.minByOrNull(selector: (T) -> R): T?(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = sequenceOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val youngest = people.minByOrNull { it.age }
println(youngest?.name)   // Bob
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/min-by-or-null.html)

    