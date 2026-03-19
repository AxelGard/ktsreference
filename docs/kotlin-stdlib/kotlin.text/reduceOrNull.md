

# reduceOrNull

Accumulates value starting with the first character and applying operation from left to right to current accumulator value and each character.

```kotlin
inline fun CharSequence.reduceOrNull(operation: (acc: Char, Char) -> Char): Char?(source)
```

```kotlin
fun main() {
    val word = "kotlin"

    // Returns the last character of the string
    val lastChar = word.reduceOrNull { _, c -> c }
    println(lastChar)   // prints: n

    // With an empty string, reduceOrNull returns null
    val empty = "".reduceOrNull { _, c -> c }
    println(empty)      // prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/reduce-or-null.html)

    