

# minOfOrNull

Returns the smallest value among all values produced by selector function applied to each element in the sequence or null if the sequence is empty.

```kotlin
inline fun <T> Sequence<T>.minOfOrNull(selector: (T) -> Double): Double?(source)
```

```kotlin
data class Person(val name: String, val salary: Double)

val people = listOf(
    Person("Alice", 5000.0),
    Person("Bob", 3500.0),
    Person("Charlie", 4500.0)
)

val lowestSalary: Double? = people.asSequence()
    .minOfOrNull { it.salary }

println("Lowest salary: $lowestSalary")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/min-of-or-null.html)

    