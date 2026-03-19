

# minOf

Returns the smallest value among all values produced by selector function applied to each character in the char sequence.

```kotlin
inline fun CharSequence.minOf(selector: (Char) -> Double): Double(source)
```

```kotlin
val text = "Hello, Kotlin!"
val minCode = text.minOf { it.code.toDouble() }
println("Smallest character code: $minCode")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/min-of.html)

    