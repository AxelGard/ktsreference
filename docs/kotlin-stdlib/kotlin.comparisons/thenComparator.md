

# thenComparator

Creates a comparator using the primary comparator and function to calculate a result of comparison.

```kotlin
inline fun <T> Comparator<T>.thenComparator(crossinline comparison: (a: T, b: T) -> Int): Comparator<T>(source)
```

```kotlin
import kotlin.Comparator
import kotlin.comparisons.thenComparator

data class Person(val name: String, val age: Int)

val people = listOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 30),
    Person("David", 25)
)

val ageThenNameComparator: Comparator<Person> =
    compareBy<Person> { it.age }
        .thenComparator { a, b -> a.name.compareTo(b.name) }

val sortedPeople = people.sortedWith(ageThenNameComparator)

println(sortedPeople)  // prints: [Person(name=Bob, age=25), Person(name=David, age=25), Person(name=Alice, age=30), Person(name=Charlie, age=30)]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/then-comparator.html)

    