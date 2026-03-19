

# compareValues

Compares two nullable Comparable values. Null is considered less than any value.

```kotlin
fun <T : Comparable<*>> compareValues(a: T?, b: T?): Int(source)
```

```kotlin
fun main() {
    // compare two integers
    println(compareValues(5, 10))   // -1  (5 < 10)

    // compare a string and a null
    println(compareValues("kotlin", null)) // 1  ("kotlin" > null)

    // compare two nulls
    println(compareValues(null, null)) // 0  (null == null)

    // compare two dates
    val date1 = java.time.LocalDate.of(2023, 1, 1)
    val date2 = java.time.LocalDate.of(2024, 1, 1)
    println(compareValues(date1, date2)) // -1  (date1 < date2)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/compare-values.html)

    