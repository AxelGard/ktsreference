

# thenBy

Creates a comparator comparing values after the primary comparator defined them equal. It uses the function to transform value to a Comparable instance for comparison.

```kotlin
inline fun <T> Comparator<T>.thenBy(crossinline selector: (T) -> Comparable<*>?): Comparator<T>(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = listOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Alice", 25),
    Person("Bob", 20)
)

val sortedPeople = people.sortedWith(compareBy<Person> { it.name }.thenBy { it.age })

println(sortedPeople)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/then-by.html)

    