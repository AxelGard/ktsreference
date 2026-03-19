

# mapOf

Returns a new read-only map with the specified contents, given as a list of pairs where the first value is the key and the second is the value.

```kotlin
fun <K, V> mapOf(vararg pairs: Pair<K, V>): Map<K, V>(source)(source)
```

```kotlin
fun main() {
    val fruitCount = mapOf(
        "Apple" to 10,
        "Banana" to 5,
        "Cherry" to 12
    )
    
    println(fruitCount["Banana"])  // prints 5
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-of.html)

    