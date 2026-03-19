

# binarySearchBy

Searches this list or its range for an element having the key returned by the specified selector function equal to the provided key value using the binary search algorithm. The list is expected to be sorted into ascending order according to the Comparable natural ordering of keys of its elements. otherwise the result is undefined.

```kotlin
inline fun <T, K : Comparable<K>> List<T>.binarySearchBy(key: K?, fromIndex: Int = 0, toIndex: Int = size, crossinline selector: (T) -> K?): Int(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    // Sorted by age in ascending order
    val people = listOf(
        Person("Bob", 25),
        Person("Alice", 30),
        Person("Charlie", 35)
    )

    // Search for a person with age 30
    val index = people.binarySearchBy(key = 30, selector = Person::age)

    if (index >= 0) {
        println("Found: ${people[index]}")
    } else {
        println("Person with age 30 not found")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/binary-search-by.html)

    