

# isHighSurrogate

Returns true if this character is a Unicode high-surrogate code unit (also known as leading-surrogate code unit).

```kotlin
expect fun Char.isHighSurrogate(): Boolean(source)
```

```kotlin
fun main() {
    // A high‑surrogate code unit (e.g., the first half of a Unicode emoji)
    val highSurrogate: Char = '\uD83D'
    // A low‑surrogate code unit (e.g., the second half of the same emoji)
    val lowSurrogate: Char = '\uDC36'

    println("Is the first character a high surrogate? ${highSurrogate.isHighSurrogate()}")
    println("Is the second character a high surrogate? ${lowSurrogate.isHighSurrogate()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-high-surrogate.html)

    