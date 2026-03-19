

# sortedByDescending

Returns a list of all elements sorted descending according to natural sort order of the value returned by specified selector function.

```kotlin
inline fun <T, R : Comparable<R>> Array<out T>.sortedByDescending(crossinline selector: (T) -> R?): List<T>(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val people = arrayOf(
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35)
    )

    val sortedByAgeDesc = people.sortedByDescending { it.age }

    sortedByAgeDesc.forEach { println("${it.name}: ${it.age}") }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sorted-by-descending.html)

    