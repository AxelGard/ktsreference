

# compareBy

Creates a comparator using the sequence of functions to calculate a result of comparison. The functions are called sequentially, receive the given values a and b and return Comparable objects. As soon as the Comparable instances returned by a function for a and b values do not compare as equal, the result of that comparison is returned from the Comparator.

```kotlin
fun <T> compareBy(vararg selectors: (T) -> Comparable<*>?): Comparator<T>(source)(source)
```

```kotlin
data class Person(val firstName: String, val lastName: String, val age: Int)

val people = listOf(
    Person("Alice", "Smith", 30),
    Person("Bob", "Johnson", 25),
    Person("Alice", "Brown", 20)
)

val sorted = people.sortedWith(compareBy<Person>(
    { it.firstName },
    { it.lastName },
    { it.age }
))

println(sorted)
// Output: [Person(firstName=Alice, lastName=Brown, age=20), Person(firstName=Alice, lastName=Smith, age=30), Person(firstName=Bob, lastName=Johnson, age=25)]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/compare-by.html)

    