

# maxByOrNull

Returns the first character yielding the largest value of the given selector function or null if there are no characters.

```kotlin
inline fun <R : Comparable<R>> CharSequence.maxByOrNull(selector: (Char) -> R): Char?(source)
```

```kotlin
val text = "Kotlin is great"
val maxChar = text.maxByOrNull { it.code }   // character with the highest Unicode code point
println("Character with highest code point: $maxChar")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/max-by-or-null.html)

    