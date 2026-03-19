

# minWith

Returns the first element having the smallest value according to the provided comparator.

```kotlin
@JvmName(name = "minWithOrThrow")fun <T> Array<out T>.minWith(comparator: Comparator<in T>): T(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = arrayOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val youngest = people.minWith(Comparator { p1, p2 -> p1.age - p2.age })
println("Youngest: ${youngest.name}, Age: ${youngest.age}")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min-with.html)

    