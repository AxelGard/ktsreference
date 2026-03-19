

# filterValues

Returns a map containing all key-value pairs with values matching the given predicate.

```kotlin
inline fun <K, V> Map<out K, V>.filterValues(predicate: (V) -> Boolean): Map<K, V>(source)
```

```kotlin
val students = mapOf(
    "Alice" to 85,
    "Bob" to 92,
    "Charlie" to 67,
    "Diana" to 78
)

val passing = students.filterValues { score -> score >= 80 }

println(passing) // prints: {Alice=85, Bob=92}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-values.html)

    