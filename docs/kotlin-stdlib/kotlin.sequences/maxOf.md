

# maxOf

Returns the largest value among all values produced by selector function applied to each element in the sequence.

```kotlin
inline fun <T> Sequence<T>.maxOf(selector: (T) -> Double): Double(source)
```

```kotlin
data class Student(val name: String, val score: Double)

val students = listOf(
    Student("Alice", 85.0),
    Student("Bob", 92.5),
    Student("Charlie", 78.0)
)

val maxScore: Double = students.asSequence().maxOf { it.score }

println("Highest score: $maxScore")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/max-of.html)

    