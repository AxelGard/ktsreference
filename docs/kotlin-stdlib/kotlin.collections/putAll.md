

# putAll

Puts all the given pairs into this MutableMap with the first component in the pair being the key and the second the value.

```kotlin
fun <K, V> MutableMap<in K, in V>.putAll(pairs: Array<out Pair<K, V>>)(source)
```

```kotlin
fun main() {
    // Existing mutable map
    val map = mutableMapOf<String, Int>()

    // Array of pairs to add
    val newPairs = arrayOf(
        "apple" to 3,
        "banana" to 5,
        "cherry" to 2
    )

    // Add all pairs to the map
    map.putAll(newPairs)

    println(map) // {apple=3, banana=5, cherry=2}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/put-all.html)

    