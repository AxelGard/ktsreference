

# foldIndexed

Accumulates value starting with initial value and applying operation from left to right to current accumulator value and each character with its index in the original char sequence.

```kotlin
inline fun <R> CharSequence.foldIndexed(initial: R, operation: (index: Int, acc: R, Char) -> R): R(source)
```

```kotlin
val input = "a1b2c3"

val sumIndices = input.foldIndexed(0) { index, acc, ch ->
    if (ch.isDigit()) acc + index else acc
}

println(sumIndices)  // Prints: 5
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/fold-indexed.html)

    