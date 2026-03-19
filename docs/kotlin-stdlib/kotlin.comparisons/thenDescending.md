

# thenDescending

Combines this comparator and the given comparator such that the latter is applied only when the former considered values equal.

```kotlin
infix fun <T> Comparator<T>.thenDescending(comparator: Comparator<in T>): Comparator<T>(source)
```

```kotlin
import kotlin.comparisons.compareBy

data class Person(val name: String, val age: Int)

val people = listOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 30),
    Person("David", 25)
)

// Comparator: first by age ascending, then by name descending
val comparator = compareBy<Person> { it.age } thenDescending compareBy<Person> { it.name }

val sortedPeople = people.sortedWith(comparator)

println(sortedPeople)
// Output: [Person(name=Bob, age=25), Person(name=David, age=25), Person(name=Charlie, age=30), Person(name=Alice, age=30)]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/then-descending.html)

    