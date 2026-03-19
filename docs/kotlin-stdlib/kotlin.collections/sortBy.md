

# sortBy

Sorts elements in the array in-place according to natural sort order of the value returned by specified selector function.

```kotlin
inline fun <T, R : Comparable<R>> Array<out T>.sortBy(crossinline selector: (T) -> R?)(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = arrayOf(
    Person("Alice",   30),
    Person("Bob",     25),
    Person("Charlie", 35)
)

people.sortBy { it.age }

println(people.joinToString { "${it.name}:${it.age}" })
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sort-by.html)

    