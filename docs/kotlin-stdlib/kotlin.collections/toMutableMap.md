

# toMutableMap

Returns a new mutable map containing all key-value pairs from the original map.

```kotlin
fun <K, V> Map<out K, V>.toMutableMap(): MutableMap<K, V>(source)
```

```kotlin
fun main() {
    val immutable = mapOf("a" to 1, "b" to 2)
    val mutable = immutable.toMutableMap()
    mutable["c"] = 3
    mutable.remove("a")
    println(mutable)   // prints {b=2, c=3}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-mutable-map.html)

    