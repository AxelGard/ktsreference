

# mapIndexedNotNull

Returns a list containing only the non-null results of applying the given transform function to each element and its index in the original array.

```kotlin
inline fun <T, R : Any> Array<out T>.mapIndexedNotNull(transform: (index: Int, T) -> R?): List<R>(source)
```

```kotlin
fun main() {
    val words = arrayOf("apple", "banana", "cherry", "date")
    val shortWords = words.mapIndexedNotNull { index, word ->
        if (word.length <= 5) "$index:$word" else null
    }
    println(shortWords) // prints: [0:apple, 3:date]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-indexed-not-null.html)

    