

# maxOfOrNull

Returns the largest value among all values produced by selector function applied to each element in the array or null if the array is empty.

```kotlin
inline fun <T> Array<out T>.maxOfOrNull(selector: (T) -> Double): Double?(source)
```

```kotlin
data class Student(val name: String, val score: Double)

val students = arrayOf(
    Student("Alice", 88.5),
    Student("Bob", 92.0),
    Student("Charlie", 79.3)
)

val highestScore = students.maxOfOrNull { it.score }   // returns 92.0
println("Highest score: $highestScore")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/max-of-or-null.html)

    