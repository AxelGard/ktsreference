

# minBy

Returns the first character yielding the smallest value of the given selector function.

```kotlin
@JvmName(name = "minByOrThrow")inline fun <R : Comparable<R>> CharSequence.minBy(selector: (Char) -> R): Char(source)
```

```kotlin
fun main() {
    val text = "Kotlin"
    // Find the character with the smallest Unicode code point
    val smallestChar = text.minBy { it.code }
    println("Smallest character: $smallestChar")   // prints 'K'
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/min-by.html)

    