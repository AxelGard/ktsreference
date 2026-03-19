

# minBy

Returns the first element yielding the smallest value of the given selector function.

```kotlin
@JvmName(name = "minByOrThrow")inline fun <T, R : Comparable<R>> Sequence<T>.minBy(selector: (T) -> R): T(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = sequenceOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val youngest = people.minBy { it.age }
println("Youngest: ${youngest.name}, age ${youngest.age}")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/min-by.html)

    