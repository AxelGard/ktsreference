

# dropWhile

Returns a list containing all elements except first elements that satisfy the given predicate.

```kotlin
inline fun <T> Array<out T>.dropWhile(predicate: (T) -> Boolean): List<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 5, 6, 7)
    val result = numbers.dropWhile { it < 5 }
    println(result) // Output: [5, 6, 7]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/drop-while.html)

    