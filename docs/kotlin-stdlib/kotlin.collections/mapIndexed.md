

# mapIndexed

Returns a list containing the results of applying the given transform function to each element and its index in the original array.

```kotlin
inline fun <T, R> Array<out T>.mapIndexed(transform: (index: Int, T) -> R): List<R>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(10, 20, 30, 40)

    // Use mapIndexed to create a list of strings that include the index and the value
    val indexedStrings = numbers.mapIndexed { index, value ->
        "Index $index has value $value"
    }

    println(indexedStrings)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-indexed.html)

    