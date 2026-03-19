

# codePointAt

Returns the character (Unicode code point) at the specified index.

```kotlin
inline fun String.codePointAt(index: Int): Int(source)
```

```kotlin
fun main() {
    val text = "Hello, 🌍!"

    // Index of the '🌍' emoji (surrogate pair)
    val index = 7

    // Get the Unicode code point at the specified index
    val codePoint: Int = text.codePointAt(index)

    // Convert the code point back to a string for display
    val character = String(Character.toChars(codePoint))

    println("Code point at index $index: U+${codePoint.toString(16).uppercase()}")
    println("Character: $character")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/code-point-at.html)

    