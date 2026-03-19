

# maxWithOrNull

Returns the first element having the largest value according to the provided comparator or null if there are no elements.

```kotlin
fun <T> Array<out T>.maxWithOrNull(comparator: Comparator<in T>): T?(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = arrayOf(
    Person("Alice",   30),
    Person("Bob",     25),
    Person("Charlie", 35)
)

val oldest = people.maxWithOrNull(compareBy { it.age })
println(oldest)   // prints: Person(name=Charlie, age=35)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/max-with-or-null.html)

    