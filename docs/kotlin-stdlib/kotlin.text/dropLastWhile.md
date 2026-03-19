

# dropLastWhile

Returns a subsequence of this char sequence containing all characters except last characters that satisfy the given predicate.

```kotlin
inline fun CharSequence.dropLastWhile(predicate: (Char) -> Boolean): CharSequence(source)
```

```kotlin
fun main() {
    val text = "Sample text!!!"
    val trimmed = text.dropLastWhile { it == '!' }
    println(trimmed) // Output: Sample text
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/drop-last-while.html)

    