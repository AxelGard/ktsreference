

# get

Returns the value corresponding to the given key, or null if such a key is not present in the map.

```kotlin
inline operator fun <K, V> Map<out K, V>.get(key: K): V?(source)
```

```kotlin
val scores = mapOf(
    "Alice" to 90,
    "Bob"   to 75,
    "Carol" to 88
)

// Retrieve a value with a key that exists
val aliceScore = scores["Alice"]
println("Alice's score: $aliceScore") // prints: Alice's score: 90

// Attempt to retrieve a value with a key that does not exist
val daveScore = scores["Dave"]
println("Dave's score: $daveScore") // prints: Dave's score: null
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/get.html)

    