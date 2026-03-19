

# toPair

Converts this map entry to a Pair with its key being the first component and its value being the second.

```kotlin
inline fun <K, V> Map.Entry<K, V>.toPair(): Pair<K, V>(source)
```

```kotlin
fun main() {
    val map = mapOf("a" to 1, "b" to 2)
    val entry = map.entries.first()
    val pair = entry.toPair()
    println(pair)  // prints: (a, 1)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-pair.html)

    