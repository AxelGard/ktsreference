

# maxOfWithOrNull

Returns the largest value according to the provided comparator among all values produced by selector function applied to each element in the array or null if the array is empty.

```kotlin
inline fun <T, R> Array<out T>.maxOfWithOrNull(comparator: Comparator<in R>, selector: (T) -> R): R?(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = arrayOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val oldestAge = people.maxOfWithOrNull(Comparator.naturalOrder()) { it.age }

println("Oldest age: $oldestAge")   // Oldest age: 35
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/max-of-with-or-null.html)

    