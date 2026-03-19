

# minusAssign

Removes the entry with the given key from this mutable map.

```kotlin
inline operator fun <K, V> MutableMap<K, V>.minusAssign(key: K)(source)
```

```kotlin
fun main() {
    val map = mutableMapOf("a" to 1, "b" to 2, "c" to 3)
    map -= "b"          // removes the entry with key "b"
    println(map)        // prints {a=1, c=3}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/minus-assign.html)

    