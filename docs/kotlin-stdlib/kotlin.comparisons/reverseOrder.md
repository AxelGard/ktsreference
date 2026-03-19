

# reverseOrder

Returns a comparator that compares Comparable objects in reversed natural order.

```kotlin
fun <T : Comparable<T>> reverseOrder(): Comparator<T>(source)
```

```kotlin
import kotlin.comparisons.reverseOrder

fun main() {
    val numbers = listOf(3, 1, 4, 1, 5)
    val sortedNumbers = numbers.sortedWith(reverseOrder())
    println(sortedNumbers)   // Output: [5, 4, 3, 1, 1]

    val words = listOf("apple", "banana", "cherry")
    val sortedWords = words.sortedWith(reverseOrder())
    println(sortedWords)     // Output: [cherry, banana, apple]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/reverse-order.html)

    