

# mapIndexed

Returns a list containing the results of applying the given transform function to each character and its index in the original char sequence.

```kotlin
inline fun <R> CharSequence.mapIndexed(transform: (index: Int, Char) -> R): List<R>(source)
```

```kotlin
fun main() {
    val text = "Kotlin"
    val indexedChars: List<String> = text.mapIndexed { index, char ->
        "$index -> $char"
    }
    println(indexedChars) // Output: [0 -> K, 1 -> o, 2 -> t, 3 -> l, 4 -> i, 5 -> n]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/map-indexed.html)

    