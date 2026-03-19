

# reversed

Returns a comparator that imposes the reverse ordering of this comparator.

```kotlin
fun <T> Comparator<T>.reversed(): Comparator<T>(source)
```

```kotlin
import kotlin.comparisons.reversed

data class Person(val name: String, val age: Int)

fun main() {
    val people = listOf(
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35)
    )

    // Comparator that sorts by age ascending
    val ageAsc = compareBy<Person> { it.age }

    // Reverse the comparator to sort by age descending
    val ageDesc = ageAsc.reversed()

    // Sort the list using the reversed comparator
    val sortedByAgeDesc = people.sortedWith(ageDesc)

    sortedByAgeDesc.forEach { println("${it.name} - ${it.age}") }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/reversed.html)

    