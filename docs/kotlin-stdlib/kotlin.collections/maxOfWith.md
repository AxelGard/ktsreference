

# maxOfWith

Returns the largest value according to the provided comparator among all values produced by selector function applied to each element in the array.

```kotlin
inline fun <T, R> Array<out T>.maxOfWith(comparator: Comparator<in R>, selector: (T) -> R): R(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val people = arrayOf(
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35)
    )

    val maxAge = people.maxOfWith(Comparator.naturalOrder<Int>(), Person::age)
    println(maxAge)   // prints: 35
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/max-of-with.html)

    