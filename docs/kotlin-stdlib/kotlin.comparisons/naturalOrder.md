

# naturalOrder

Returns a comparator that compares Comparable objects in natural order.

```kotlin
fun <T : Comparable<T>> naturalOrder(): Comparator<T>(source)
```

```kotlin
import kotlin.comparisons.naturalOrder

fun main() {
    // Example 1: Sorting a list of integers
    val numbers = listOf(3, 1, 4, 1, 5, 9, 2, 6, 5)
    val numberComparator = naturalOrder<Int>()
    val sortedNumbers = numbers.sortedWith(numberComparator)
    println(sortedNumbers)  // Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]

    // Example 2: Sorting a list of strings
    val words = listOf("banana", "apple", "orange", "mango")
    val stringComparator = naturalOrder<String>()
    val sortedWords = words.sortedWith(stringComparator)
    println(sortedWords)  // Output: [apple, banana, mango, orange]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/natural-order.html)

    