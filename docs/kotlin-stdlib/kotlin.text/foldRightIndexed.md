

# foldRightIndexed

Accumulates value starting with initial value and applying operation from right to left to each character with its index in the original char sequence and current accumulator value.

```kotlin
inline fun <R> CharSequence.foldRightIndexed(initial: R, operation: (index: Int, Char, acc: R) -> R): R(source)
```

```kotlin
fun main() {
    val text = "abc"
    val result = text.foldRightIndexed("") { index, char, acc ->
        "$acc$index:$char "
    }
    println(result)   // prints: 0:a 1:b 2:c 
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/fold-right-indexed.html)

    