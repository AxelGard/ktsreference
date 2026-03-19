

# minByOrNull

Returns the first element yielding the smallest value of the given selector function or null if there are no elements.

```kotlin
inline fun <T, R : Comparable<R>> Array<out T>.minByOrNull(selector: (T) -> R): T?(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = arrayOf(
    Person("Alice", 30),
    Person("Bob", 24),
    Person("Charlie", 35)
)

val youngest = people.minByOrNull { it.age }

println(youngest?.name)   // Prints: Bob
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min-by-or-null.html)

    