

# foldRight

Accumulates value starting with initial value and applying operation from right to left to each character and current accumulator value.

```kotlin
inline fun <R> CharSequence.foldRight(initial: R, operation: (Char, acc: R) -> R): R(source)
```

```kotlin
fun main() {
    val text = "Kotlin"
    // Sum of ASCII values of the characters
    val sum = text.foldRight(0) { ch, acc -> acc + ch.code }
    println("Sum of ASCII codes: $sum")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/fold-right.html)

    