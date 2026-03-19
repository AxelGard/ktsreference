

# groupingBy

Creates a Grouping source from an array to be used later with one of group-and-fold operations using the specified keySelector function to extract a key from each element.

```kotlin
inline fun <T, K> Array<out T>.groupingBy(crossinline keySelector: (T) -> K): Grouping<T, K>(source)
```

```kotlin
fun main() {
    val words = arrayOf("apple", "apricot", "banana", "avocado")
    val counts = words.groupingBy { it[0] }.eachCount()
    println(counts)  // Output: {a=3, b=1}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/grouping-by.html)

    