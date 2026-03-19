

# nullsFirst

Extends the given comparator of non-nullable values to a comparator of nullable values considering null value less than any other value. Non-null values are compared with the provided comparator.

```kotlin
fun <T : Any> nullsFirst(comparator: Comparator<in T>): Comparator<T?>(source)
```

```kotlin
import kotlin.comparisons.nullsFirst

fun main() {
    val values = listOf(5, null, 3, null, 1)

    val sorted = values.sortedWith(
        nullsFirst(Comparator<Int> { a, b -> a.compareTo(b) })
    )

    println(sorted)   // [null, null, 1, 3, 5]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/nulls-first.html)

    