

# dropWhile

Returns a subsequence of this char sequence containing all characters except first characters that satisfy the given predicate.

```kotlin
inline fun CharSequence.dropWhile(predicate: (Char) -> Boolean): CharSequence(source)
```

```kotlin
fun main() {
    val text = "   Kotlin"
    val trimmed = text.dropWhile { it == ' ' }
    println(trimmed) // Output: Kotlin
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/drop-while.html)

    