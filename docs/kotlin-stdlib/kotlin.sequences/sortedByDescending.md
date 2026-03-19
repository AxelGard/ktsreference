

# sortedByDescending

Returns a sequence that yields elements of this sequence sorted descending according to natural sort order of the value returned by specified selector function.

```kotlin
inline fun <T, R : Comparable<R>> Sequence<T>.sortedByDescending(crossinline selector: (T) -> R?): Sequence<T>(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val people = listOf(
        Person("Alice", 29),
        Person("Bob", 34),
        Person("Charlie", 23),
        Person("Diana", 34)
    )

    val descendingByAge: Sequence<Person> =
        people.asSequence().sortedByDescending { it.age }

    descendingByAge.forEach { println("${it.name} (${it.age})") }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sorted-by-descending.html)

    