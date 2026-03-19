

# sortedMapOf

Returns a new SortedMap with the specified contents, given as a list of pairs where the first value is the key and the second is the value.

```kotlin
fun <K : Comparable<K>, V> sortedMapOf(vararg pairs: Pair<K, V>): SortedMap<K, V>(source)
```

```kotlin
val fruitCounts = sortedMapOf(
    "banana" to 5,
    "apple" to 10,
    "cherry" to 3
)

println(fruitCounts) // {apple=10, banana=5, cherry=3}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sorted-map-of.html)

    