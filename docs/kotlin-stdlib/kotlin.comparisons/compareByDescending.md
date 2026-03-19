

# compareByDescending

Creates a descending comparator using the function to transform value to a Comparable instance for comparison.

```kotlin
inline fun <T> compareByDescending(crossinline selector: (T) -> Comparable<*>?): Comparator<T>(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = listOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val sortedByAgeDesc = people.sortedWith(compareByDescending<Person> { it.age })

println(sortedByAgeDesc)   // [Person(name=Charlie, age=35), Person(name=Alice, age=30), Person(name=Bob, age=25)]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/compare-by-descending.html)

    