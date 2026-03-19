

# indexOfLast

Returns index of the last element matching the given predicate, or -1 if the array does not contain such element.

```kotlin
inline fun <T> Array<out T>.indexOfLast(predicate: (T) -> Boolean): Int(source)
```

```kotlin
fun main() {
    val fruits = arrayOf("apple", "banana", "cherry", "banana", "date")

    // Find the index of the last occurrence of "banana"
    val lastBananaIndex = fruits.indexOfLast { it == "banana" }

    println("Last index of 'banana': $lastBananaIndex")   // Prints: Last index of 'banana': 3

    // If the element is not found, the result is -1
    val lastFigIndex = fruits.indexOfLast { it == "fig" }
    println("Last index of 'fig': $lastFigIndex")        // Prints: Last index of 'fig': -1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/index-of-last.html)

    