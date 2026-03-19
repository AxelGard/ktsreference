

# mapIndexedNotNull

Returns a list containing only the non-null results of applying the given transform function to each character and its index in the original char sequence.

```kotlin
inline fun <R : Any> CharSequence.mapIndexedNotNull(transform: (index: Int, Char) -> R?): List<R>(source)
```

```kotlin
val text = "hello world 123"

val digitIndices = text.mapIndexedNotNull { index, char ->
    if (char.isDigit()) index else null
}

println(digitIndices)   // [15, 16, 17]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/map-indexed-not-null.html)

    