

# groupBy

Groups elements of the original array by the key returned by the given keySelector function applied to each element and returns a map where each group key is associated with a list of corresponding elements.

```kotlin
inline fun <T, K> Array<out T>.groupBy(keySelector: (T) -> K): Map<K, List<T>>(source)
```

```kotlin
fun main() {
    val words = arrayOf("apple", "apricot", "banana", "blueberry", "cherry")
    val grouped = words.groupBy { it.first() }   // group by first letter
    println(grouped)   // {a=[apple, apricot], b=[banana, blueberry], c=[cherry]}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/group-by.html)

    