

# filterIndexed

Returns a list containing only elements matching the given predicate.

```kotlin
inline fun <T> Array<out T>.filterIndexed(predicate: (index: Int, T) -> Boolean): List<T>(source)
```

```kotlin
fun main() {
    val words = arrayOf("apple", "banana", "cherry", "date", "elderberry")
    val filtered = words.filterIndexed { index, _ -> index % 2 == 0 }
    println(filtered) // [apple, cherry, elderberry]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-indexed.html)

    