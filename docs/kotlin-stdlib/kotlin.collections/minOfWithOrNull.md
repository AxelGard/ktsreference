

# minOfWithOrNull

Returns the smallest value according to the provided comparator among all values produced by selector function applied to each element in the array or null if the array is empty.

```kotlin
inline fun <T, R> Array<out T>.minOfWithOrNull(comparator: Comparator<in R>, selector: (T) -> R): R?(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val people = arrayOf(
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35)
    )

    // Find the smallest age among all people (or null if the array is empty)
    val youngestAge: Int? = people.minOfWithOrNull(Comparator.naturalOrder(), { it.age })

    println("Youngest age: $youngestAge")   // Output: Youngest age: 25
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min-of-with-or-null.html)

    