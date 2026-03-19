

# firstNotNullOfOrNull

Returns the first non-null value produced by transform function being applied to characters of this char sequence in iteration order, or null if no non-null value was produced.

```kotlin
inline fun <R : Any> CharSequence.firstNotNullOfOrNull(transform: (Char) -> R?): R?(source)
```

```kotlin
fun main() {
    val text = "abc123def"
    val firstNumber: Int? = text.firstNotNullOfOrNull { ch ->
        if (ch.isDigit()) ch.digitToInt() else null
    }
    println(firstNumber) // prints: 1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/first-not-null-of-or-null.html)

    