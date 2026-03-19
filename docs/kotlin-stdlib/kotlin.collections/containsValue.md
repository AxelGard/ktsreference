

# containsValue

Returns true if the map maps one or more keys to the specified value.

```kotlin
inline fun <K, V> Map<K, V>.containsValue(value: V): Boolean(source)
```

```kotlin
fun main() {
    val map = mapOf(
        "apple" to 10,
        "banana" to 20,
        "cherry" to 30
    )

    // Check if a value is present in the map
    println(map.containsValue(20)) // true
    println(map.containsValue(40)) // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/contains-value.html)

    