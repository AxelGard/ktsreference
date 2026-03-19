

# minOfOrNull

Returns the smallest value among all values produced by selector function applied to each character in the char sequence or null if the char sequence is empty.

```kotlin
inline fun CharSequence.minOfOrNull(selector: (Char) -> Double): Double?(source)
```

```kotlin
val text = "Kotlin"

val smallestCharCode = text.minOfOrNull { it.code.toDouble() }

println(smallestCharCode)  // prints the smallest Unicode code point value in the string
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/min-of-or-null.html)

    