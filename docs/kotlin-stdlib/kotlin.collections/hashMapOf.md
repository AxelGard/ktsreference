

# hashMapOf

Returns an empty new HashMap.

```kotlin
inline fun <K, V> hashMapOf(): HashMap<K, V>(source)
```

```kotlin
fun main() {
    // Create a HashMap with initial values
    val fruitCounts = hashMapOf(
        "apple"  to 3,
        "banana" to 5
    )

    // Add a new entry
    fruitCounts["orange"] = 2

    // Retrieve a value
    val apples = fruitCounts["apple"] ?: 0
    println("Number of apples: $apples")

    // Print the entire map
    println(fruitCounts) // {apple=3, banana=5, orange=2}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/hash-map-of.html)

    