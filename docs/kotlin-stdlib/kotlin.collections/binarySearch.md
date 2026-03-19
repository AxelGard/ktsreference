

# binarySearch

Searches this list or its range for the provided element using the binary search algorithm. The list is expected to be sorted into ascending order according to the Comparable natural ordering of its elements, otherwise the result is undefined.

```kotlin
fun <T : Comparable<T>> List<T?>.binarySearch(element: T?, fromIndex: Int = 0, toIndex: Int = size): Int(source)
```

```kotlin
fun main() {
    val numbers = listOf(1, 3, 5, 7, 9)

    // Search for an existing element
    val index = numbers.binarySearch(5)
    println("Index of 5: $index")            // Output: 2

    // Search for a non‑existing element
    val missing = numbers.binarySearch(4)
    println("Index of 4: $missing")          // Output: -3 (-(insertion point) - 1)

    // Search within a subrange (fromIndex = 2)
    val subIndex = numbers.binarySearch(7, fromIndex = 2)
    println("Index of 7 in subrange: $subIndex") // Output: 3
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/binary-search.html)

    