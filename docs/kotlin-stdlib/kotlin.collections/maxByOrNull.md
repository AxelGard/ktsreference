

# maxByOrNull

Returns the first element yielding the largest value of the given selector function or null if there are no elements.

```kotlin
inline fun <T, R : Comparable<R>> Array<out T>.maxByOrNull(selector: (T) -> R): T?(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val people = arrayOf(
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35)
    )

    val oldest = people.maxByOrNull { it.age }
    println(oldest?.name) // prints: Charlie
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/max-by-or-null.html)

    