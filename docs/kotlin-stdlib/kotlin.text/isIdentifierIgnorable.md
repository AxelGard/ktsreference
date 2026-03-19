

# isIdentifierIgnorable

Returns true if this character (Unicode code point) should be regarded as an ignorable character in a Java identifier or a Unicode identifier.

```kotlin
inline fun Char.isIdentifierIgnorable(): Boolean(source)
```

```kotlin
fun main() {
    val example = "Kotlin\u200BCode"   // \u200B is a zero‑width space (ignorable)
    val ignorableChars = example.filter { it.isIdentifierIgnorable() }
    println("Ignorable characters: $ignorableChars")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-identifier-ignorable.html)

    