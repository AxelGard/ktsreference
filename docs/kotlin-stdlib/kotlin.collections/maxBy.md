

# maxBy

Returns the first element yielding the largest value of the given selector function.

```kotlin
@JvmName(name = "maxByOrThrow")inline fun <T, R : Comparable<R>> Array<out T>.maxBy(selector: (T) -> R): T(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = arrayOf(
    Person("Alice", 28),
    Person("Bob", 35),
    Person("Charlie", 22)
)

val oldest = people.maxBy { it.age }
println(oldest.name)   // Bob
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/max-by.html)

    