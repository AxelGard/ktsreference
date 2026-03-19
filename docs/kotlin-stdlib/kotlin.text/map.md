

# map

Returns a list containing the results of applying the given transform function to each character in the original char sequence.

```kotlin
inline fun <R> CharSequence.map(transform: (Char) -> R): List<R>(source)
```

```kotlin
fun main() {
    val text = "Kotlin"

    // Map each character to its Unicode code point
    val codePoints: List<Int> = text.map { it.code }

    println("Original text: $text")
    println("Code points: $codePoints")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/map.html)

    