

# toMap

Returns a new map containing all key-value pairs from the given collection of pairs.

```kotlin
fun <K, V> Iterable<Pair<K, V>>.toMap(): Map<K, V>(source)
```

```kotlin
val pairs = listOf(
    "apple" to 5,
    "banana" to 3,
    "orange" to 7
)

val fruitCountMap: Map<String, Int> = pairs.toMap()

println(fruitCountMap) // {apple=5, banana=3, orange=7}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-map.html)

    