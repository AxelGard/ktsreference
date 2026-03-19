

# maxOf

Returns the largest value among all values produced by selector function applied to each element in the array.

```kotlin
inline fun <T> Array<out T>.maxOf(selector: (T) -> Double): Double(source)
```

```kotlin
data class Person(val name: String, val height: Double)

val people = arrayOf(
    Person("Alice", 1.65),
    Person("Bob", 1.82),
    Person("Charlie", 1.75)
)

val tallestHeight = people.maxOf { it.height }
println("Tallest height: $tallestHeight")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/max-of.html)

    