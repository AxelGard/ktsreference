

# thenByDescending

Creates a descending comparator using the primary comparator and the function to transform value to a Comparable instance for comparison.

```kotlin
inline fun <T> Comparator<T>.thenByDescending(crossinline selector: (T) -> Comparable<*>?): Comparator<T>(source)
```

```kotlin
data class Person(val name: String, val age: Int, val salary: Double)

val people = listOf(
    Person("Alice", 30, 50000.0),
    Person("Bob", 25, 60000.0),
    Person("Alice", 25, 70000.0),
    Person("Bob", 30, 55000.0)
)

val sorted = people.sortedWith(
    compareBy<Person> { it.name }          // primary (ascending) sort by name
        .thenByDescending { it.age }       // secondary (descending) sort by age
)

println(sorted)
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/then-by-descending.html)

    