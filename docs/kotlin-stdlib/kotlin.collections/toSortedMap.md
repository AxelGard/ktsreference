

# toSortedMap

Converts this Map to a SortedMap. The resulting SortedMap determines the equality and order of keys according to their natural sorting order.

```kotlin
fun <K : Comparable<K>, V> Map<out K, V>.toSortedMap(): SortedMap<K, V>(source)
```

```kotlin
fun main() {
    val unsorted = mapOf(5 to "five", 3 to "three", 8 to "eight")
    val sorted: SortedMap<Int, String> = unsorted.toSortedMap()
    println(sorted)  // Output: {3=three, 5=five, 8=eight}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-sorted-map.html)

    