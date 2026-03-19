

# getOrDefault

Returns the value to which the specified key is mapped, or defaultValue if this map contains no mapping for the key.

```kotlin
inline fun <K, V> Map<out K, V>.getOrDefault(key: K, defaultValue: V): V(source)
```

```kotlin
fun main() {
    val scores = mapOf("Alice" to 90, "Bob" to 75)
    val charlieScore = scores.getOrDefault("Charlie", 0)
    println("Charlie's score: $charlieScore")  // prints: Charlie's score: 0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/get-or-default.html)

    