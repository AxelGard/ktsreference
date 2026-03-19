

# isLetterOrDigit

Returns true if this character is a letter or digit.

```kotlin
expect fun Char.isLetterOrDigit(): Boolean(source)
```

fun main() {
    val text = "Kotlin 2024!"
    val cleaned = text.filter { it.isLetterOrDigit() }
    println(cleaned)   // Prints: Kotlin2024
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-letter-or-digit.html)

    