

# reduce

Accumulates value starting with the first character and applying operation from left to right to current accumulator value and each character.

```kotlin
inline fun CharSequence.reduce(operation: (acc: Char, Char) -> Char): Char(source)
```

fun main() {
    val text = "Kotlin"
    val maxChar = text.reduce { acc, c -> if (c > acc) c else acc }
    println("Max character: $maxChar")  // Output: Max character: t
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/reduce.html)

    