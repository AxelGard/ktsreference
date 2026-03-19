

# firstNotNullOf

Returns the first non-null value produced by transform function being applied to characters of this char sequence in iteration order, or throws NoSuchElementException if no non-null value was produced.

```kotlin
inline fun <R : Any> CharSequence.firstNotNullOf(transform: (Char) -> R?): R(source)
```

```kotlin
fun main() {
    val text = "Kotlin"

    // Find the first uppercase letter in the string
    val firstUpper = text.firstNotNullOf { ch ->
        if (ch.isUpperCase()) ch else null
    }

    println(firstUpper)   // prints: K
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/first-not-null-of.html)

    