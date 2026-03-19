

# sorted

Returns a list of all elements sorted according to their natural sort order.

```kotlin
fun <T : Comparable<T>> Array<out T>.sorted(): List<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(3, 1, 4, 1, 5)
    val sortedNumbers = numbers.sorted()
    println(sortedNumbers)   // Output: [1, 1, 3, 4, 5]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sorted.html)

    