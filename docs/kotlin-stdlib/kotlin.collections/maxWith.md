

# maxWith

Returns the first element having the largest value according to the provided comparator.

```kotlin
@JvmName(name = "maxWithOrThrow")fun <T> Array<out T>.maxWith(comparator: Comparator<in T>): T(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = arrayOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val oldest = people.maxWith(compareBy<Person> { it.age })

println("Oldest: ${oldest.name}, age ${oldest.age}")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/max-with.html)

    