

# sortedBy

Returns a list of all elements sorted according to natural sort order of the value returned by specified selector function.

```kotlin
inline fun <T, R : Comparable<R>> Array<out T>.sortedBy(crossinline selector: (T) -> R?): List<T>(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = arrayOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val sortedByAge: List<Person> = people.sortedBy { it.age }

println(sortedByAge)   // [Person(name=Bob, age=25), Person(name=Alice, age=30), Person(name=Charlie, age=35)]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sorted-by.html)

    