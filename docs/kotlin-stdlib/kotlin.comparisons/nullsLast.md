

# nullsLast

Extends the given comparator of non-nullable values to a comparator of nullable values considering null value greater than any other value. Non-null values are compared with the provided comparator.

```kotlin
fun <T : Any> nullsLast(comparator: Comparator<in T>): Comparator<T?>(source)
```

```kotlin
import kotlin.comparisons.nullsLast
import kotlin.Comparator

fun main() {
    val values: List<String?> = listOf("pear", null, "apple", "banana", null)

    val sorted = values.sortedWith(
        nullsLast(Comparator.naturalOrder<String>())
    )

    println(sorted)   // [apple, banana, pear, null, null]
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/nulls-last.html)

    