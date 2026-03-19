

# mapNotNull

Returns a list containing only the non-null results of applying the given transform function to each character in the original char sequence.

```kotlin
inline fun <R : Any> CharSequence.mapNotNull(transform: (Char) -> R?): List<R>(source)
```

```kotlin
fun main() {
    val text = "abc123def456"
    val digits = text.mapNotNull { 
        if (it.isDigit()) it.toString().toInt() else null 
    }
    println(digits)   // Output: [1, 2, 3, 4, 5, 6]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/map-not-null.html)

    