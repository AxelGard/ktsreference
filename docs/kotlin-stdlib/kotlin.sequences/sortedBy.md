

# sortedBy

Returns a sequence that yields elements of this sequence sorted according to natural sort order of the value returned by specified selector function.

```kotlin
inline fun <T, R : Comparable<R>> Sequence<T>.sortedBy(crossinline selector: (T) -> R?): Sequence<T>(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val people = listOf(
        Person("Alice", 32),
        Person("Bob", 25),
        Person("Charlie", 28)
    )

    val sortedByAge = people.asSequence()
        .sortedBy { it.age }
        .toList()

    println(sortedByAge)   // [Person(name=Bob, age=25), Person(name=Charlie, age=28), Person(name=Alice, age=32)]
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sorted-by.html)

    