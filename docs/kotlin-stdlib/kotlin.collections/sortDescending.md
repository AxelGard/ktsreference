

# sortDescending

Sorts elements in the array in-place descending according to their natural sort order.

```kotlin
fun <T : Comparable<T>> Array<out T>.sortDescending()(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(5, 3, 8, 1, 4)
    numbers.sortDescending()
    println(numbers.joinToString())   // prints: 8, 5, 4, 3, 1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sort-descending.html)

    