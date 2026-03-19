

# minOf

Returns the smallest value among all values produced by selector function applied to each element in the array.

```kotlin
inline fun <T> Array<out T>.minOf(selector: (T) -> Double): Double(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val people = arrayOf(
        Person("Alice", 28),
        Person("Bob", 34),
        Person("Charlie", 23)
    )

    val youngestAge = people.minOf { it.age.toDouble() }
    println("Youngest age: $youngestAge")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min-of.html)

    