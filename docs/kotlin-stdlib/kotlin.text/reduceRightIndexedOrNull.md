

# reduceRightIndexedOrNull

Accumulates value starting with the last character and applying operation from right to left to each character with its index in the original char sequence and current accumulator value.

```kotlin
inline fun CharSequence.reduceRightIndexedOrNull(operation: (index: Int, Char, acc: Char) -> Char): Char?(source)
```

```kotlin
fun main() {
    val text = "kotlin"

    // Find the character with the highest code point by scanning from right to left
    val maxChar: Char? = text.reduceRightIndexedOrNull { index, current, acc ->
        if (current > acc) current else acc
    }

    println(maxChar)   // Prints: t
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/reduce-right-indexed-or-null.html)

    