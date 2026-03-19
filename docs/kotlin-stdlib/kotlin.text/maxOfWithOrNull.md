

# maxOfWithOrNull

Returns the largest value according to the provided comparator among all values produced by selector function applied to each character in the char sequence or null if the char sequence is empty.

```kotlin
inline fun <R> CharSequence.maxOfWithOrNull(comparator: Comparator<in R>, selector: (Char) -> R): R?(source)
```

```kotlin
val text = "kotlin"
val maxChar = text.maxOfWithOrNull(Comparator.naturalOrder<Char>()) { it }
println(maxChar)   // prints: t
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/max-of-with-or-null.html)

    