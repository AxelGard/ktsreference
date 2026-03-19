

# sumByDouble

Warning since 1.5

```kotlin
inline fun <T> Sequence<T>.sumByDouble(selector: (T) -> Double): Double(source)
```

```kotlin
data class Employee(val name: String, val salary: Double)

val employees = listOf(
    Employee("Alice", 5000.0),
    Employee("Bob", 6000.0),
    Employee("Carol", 7000.0)
).asSequence()

val totalSalary = employees.sumByDouble { it.salary }
println("Total salary: $totalSalary")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sum-by-double.html)

    