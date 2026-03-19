

# minOfWith

Returns the smallest value according to the provided comparator among all values produced by selector function applied to each character in the char sequence.

```kotlin
inline fun <R> CharSequence.minOfWith(comparator: Comparator<in R>, selector: (Char) -> R): R(source)
```

```kotlin
val text = "Kotlin"

val minCharIgnoringCase = text.minOfWith(
    compareBy<Char> { it.lowercaseChar() }   // Comparator that ignores case
) { it }                                   // Selector returns the char itself

println(minCharIgnoringCase)   // prints: K
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/min-of-with.html)

    