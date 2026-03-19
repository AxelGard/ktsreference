

# remove

Removes the specified key and its corresponding value from this map.

```kotlin
@IgnorableReturnValueinline fun <K, V> MutableMap<out K, V>.remove(key: K): V?(source)
```

```kotlin
fun main() {
    val scores = mutableMapOf(
        "Alice" to 90,
        "Bob" to 75,
        "Charlie" to 82
    )

    // Remove Bob's score from the map
    val removedScore: Int? = scores.remove("Bob")

    println("Removed score: $removedScore")  // Output: Removed score: 75
    println("Remaining map: $scores")        // Output: Remaining map: {Alice=90, Charlie=82}
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/remove.html)

    