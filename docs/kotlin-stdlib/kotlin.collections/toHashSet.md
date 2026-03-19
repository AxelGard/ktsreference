

# toHashSet

Returns a new HashSet of all elements.

```kotlin
fun <T> Array<out T>.toHashSet(): HashSet<T>(source)
```

```kotlin
fun main() {
    val array = arrayOf("apple", "banana", "apple", "orange")
    val set = array.toHashSet()
    println(set) // [apple, banana, orange]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-hash-set.html)

    