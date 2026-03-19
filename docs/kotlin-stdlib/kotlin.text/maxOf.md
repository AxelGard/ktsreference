

# maxOf

Returns the largest value among all values produced by selector function applied to each character in the char sequence.

```kotlin
inline fun CharSequence.maxOf(selector: (Char) -> Double): Double(source)
```

```kotlin
val text = "Hello, World!"

// Find the largest ASCII code value among all characters in the string.
val maxAscii = text.maxOf { it.code.toDouble() }

println("Maximum ASCII value in the string: $maxAscii")   // prints 119 (for 'w')
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/max-of.html)

    