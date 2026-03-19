

# offsetByCodePoints

Returns the index within this string that is offset from the given index by codePointOffset code points.

```kotlin
inline fun String.offsetByCodePoints(index: Int, codePointOffset: Int): Int(source)
```

```kotlin
fun main() {
    val text = "Hello 👋 World"
    // index of the space after "Hello"
    val startIndex = text.indexOf(' ')
    // Move forward by 1 code point (skips the emoji 👋)
    val afterEmoji = text.offsetByCodePoints(startIndex, 1)
    println(text.substring(startIndex, afterEmoji)) // prints " 👋"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/offset-by-code-points.html)

    