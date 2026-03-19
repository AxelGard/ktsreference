

# plusAssign

Appends or replaces the given pair in this mutable map.

```kotlin
inline operator fun <K, V> MutableMap<in K, in V>.plusAssign(pair: Pair<K, V>)(source)
```

```kotlin
val scores = mutableMapOf<String, Int>()

// Add entries using plusAssign (+=)
scores += "Alice" to 85
scores += "Bob" to 92

// Update an existing entry
scores += "Alice" to 90

println(scores)  // Output: {Alice=90, Bob=92}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/plus-assign.html)

    