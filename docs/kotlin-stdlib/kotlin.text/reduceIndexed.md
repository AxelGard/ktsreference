

# reduceIndexed

Accumulates value starting with the first character and applying operation from left to right to current accumulator value and each character with its index in the original char sequence.

```kotlin
inline fun CharSequence.reduceIndexed(operation: (index: Int, acc: Char, Char) -> Char): Char(source)
```

val text = "kotlin"
val maxChar = text.reduceIndexed { index, acc, c ->
    if (c > acc) c else acc
}
println("Maximum character: $maxChar")

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/reduce-indexed.html)

    