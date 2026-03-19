

# minOfWithOrNull

Returns the smallest value according to the provided comparator among all values produced by selector function applied to each character in the char sequence or null if the char sequence is empty.

```kotlin
inline fun <R> CharSequence.minOfWithOrNull(comparator: Comparator<in R>, selector: (Char) -> R): R?(source)
```

```kotlin
val text = "Kotlin 1.8!"
val smallestCodePoint = text.minOfWithOrNull(Comparator<Int> { a, b -> a.compareTo(b) }) { it.code }
println(smallestCodePoint)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/min-of-with-or-null.html)

    