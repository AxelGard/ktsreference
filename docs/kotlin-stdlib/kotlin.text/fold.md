

# fold

Accumulates value starting with initial value and applying operation from left to right to current accumulator value and each character.

```kotlin
inline fun <R> CharSequence.fold(initial: R, operation: (acc: R, Char) -> R): R(source)
```

```kotlin
fun main() {
    val text = "Hello, Kotlin!"
    val vowelCount = text.fold(0) { acc, c ->
        acc + if (c.lowercaseChar() in "aeiou") 1 else 0
    }
    println("Number of vowels in \"$text\": $vowelCount") // Output: 4
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/fold.html)

    