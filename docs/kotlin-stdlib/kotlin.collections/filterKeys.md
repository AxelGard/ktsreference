

# filterKeys

Returns a map containing all key-value pairs with keys matching the given predicate.

```kotlin
inline fun <K, V> Map<out K, V>.filterKeys(predicate: (K) -> Boolean): Map<K, V>(source)
```

```kotlin
fun main() {
    val fruits = mapOf("apple" to 5, "banana" to 3, "pear" to 4, "peach" to 2)
    val fruitsStartingWithP = fruits.filterKeys { it.startsWith("p") }
    println(fruitsStartingWithP) // {pear=4, peach=2}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-keys.html)

    