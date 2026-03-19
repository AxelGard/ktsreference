

# reduceIndexedOrNull

Accumulates value starting with the first character and applying operation from left to right to current accumulator value and each character with its index in the original char sequence.

```kotlin
inline fun CharSequence.reduceIndexedOrNull(operation: (index: Int, acc: Char, Char) -> Char): Char?(source)
```

```kotlin
fun main() {
    val text = "kotlin"
    val result = text.reduceIndexedOrNull { index, acc, current ->
        // Keep the accumulator for even indices, otherwise take the current character
        if (index % 2 == 0) acc else current
    }
    println(result) // prints: n

    val empty = "".reduceIndexedOrNull { _, _, _ -> 'X' }
    println(empty)  // prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/reduce-indexed-or-null.html)

    