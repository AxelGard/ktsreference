

# reduceRightIndexed

Accumulates value starting with the last character and applying operation from right to left to each character with its index in the original char sequence and current accumulator value.

```kotlin
inline fun CharSequence.reduceRightIndexed(operation: (index: Int, Char, acc: Char) -> Char): Char(source)
```

```kotlin
val text = "kotlin"
val maxChar = text.reduceRightIndexed { index, current, acc ->
    if (current > acc) current else acc
}
println("Maximum character: $maxChar")   // Prints: Maximum character: t
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/reduce-right-indexed.html)

    