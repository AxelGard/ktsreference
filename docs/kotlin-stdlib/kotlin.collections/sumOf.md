

# sumOf

Returns the sum of all values produced by selector function applied to each element in the array.

```kotlin
@JvmName(name = "sumOfDouble")inline fun <T> Array<out T>.sumOf(selector: (T) -> Double): Double(source)
```

```kotlin
data class Person(val name: String, val salary: Double)

val employees = arrayOf(
    Person("Alice",   5000.0),
    Person("Bob",     6000.0),
    Person("Charlie", 5500.0)
)

val totalSalary = employees.sumOf { it.salary }
println("Total salary: $totalSalary")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sum-of.html)

    