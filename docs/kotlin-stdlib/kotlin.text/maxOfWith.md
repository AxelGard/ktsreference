

# maxOfWith

Returns the largest value according to the provided comparator among all values produced by selector function applied to each character in the char sequence.

```kotlin
inline fun <R> CharSequence.maxOfWith(comparator: Comparator<in R>, selector: (Char) -> R): R(source)
```

```kotlin
val text = "Kotlin 123"

// Find the character with the highest Unicode value in the string
val maxChar = text.maxOfWith(compareBy<Char> { it }) { c -> c }

println(maxChar)   // Output: t
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/max-of-with.html)

    