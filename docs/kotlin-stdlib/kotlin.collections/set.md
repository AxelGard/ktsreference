

# set

Allows to use the index operator for storing values in a mutable map.

```kotlin
inline operator fun <K, V> MutableMap<K, V>.set(key: K, value: V)(source)
```

```kotlin
fun main() {
    val scores = mutableMapOf<String, Int>()

    // Add entries
    scores["Alice"] = 90
    scores["Bob"] = 85

    // Update an existing entry
    scores["Alice"] = 95

    println(scores)  // Output: {Alice=95, Bob=85}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/set.html)

    