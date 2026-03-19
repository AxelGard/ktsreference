

# reduceRightOrNull

Accumulates value starting with the last character and applying operation from right to left to each character and current accumulator value.

```kotlin
inline fun CharSequence.reduceRightOrNull(operation: (Char, acc: Char) -> Char): Char?(source)
```

```kotlin
val text = "Kotlin"

val firstUpperFromRight = text.reduceRightOrNull { ch, acc ->
    if (ch.isUpperCase()) ch else acc
}

println(firstUpperFromRight)   // Prints: K
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/reduce-right-or-null.html)

    