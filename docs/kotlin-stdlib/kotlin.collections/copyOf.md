

# copyOf

Returns new array which is a copy of the original array, resized to the given newSize. The copy is either truncated or padded at the end with values calculated by calling the specified init function.

```kotlin
@ExperimentalStdlibApiinline fun <T> Array<T>.copyOf(newSize: Int, init: (Int) -> T): Array<T>(source)
```

```kotlin
@OptIn(ExperimentalStdlibApi::class)
fun main() {
    val original = arrayOf("apple", "banana", "cherry")

    // Truncate the array to 2 elements
    val truncated = original.copyOf(2) { it }
    println(truncated.contentToString())   // ["apple", "banana"]

    // Pad the array to 5 elements, filling new positions with a default value
    val padded = original.copyOf(5) { index ->
        if (index < original.size) original[index]
        else "default$index"
    }
    println(padded.contentToString())     // ["apple", "banana", "cherry", "default3", "default4"]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/copy-of.html)

    