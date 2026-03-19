

# minWithOrNull

Returns the first element having the smallest value according to the provided comparator or null if there are no elements.

```kotlin
fun <T> Array<out T>.minWithOrNull(comparator: Comparator<in T>): T?(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val people = arrayOf(
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35)
    )

    val youngest = people.minWithOrNull(compareBy { it.age })
    println(youngest)   // Output: Person(name=Bob, age=25)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min-with-or-null.html)

    