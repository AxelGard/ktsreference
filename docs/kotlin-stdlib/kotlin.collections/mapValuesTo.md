

# mapValuesTo

Populates the given destination map with entries having the keys of this map and the values obtained by applying the transform function to each entry in this Map.

```kotlin
@IgnorableReturnValueinline fun <K, V, R, M : MutableMap<in K, in R>> Map<out K, V>.mapValuesTo(destination: M, transform: (Map.Entry<K, V>) -> R): M(source)
```

```kotlin
fun main() {
    val original = mapOf("apple" to 2, "banana" to 3, "cherry" to 5)
    val destination = mutableMapOf<String, Int>()

    original.mapValuesTo(destination) { entry ->
        // multiply each value by 10
        entry.value * 10
    }

    println(destination) // Output: {apple=20, banana=30, cherry=50}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-values-to.html)

    