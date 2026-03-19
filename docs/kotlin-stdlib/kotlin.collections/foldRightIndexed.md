

# foldRightIndexed

Accumulates value starting with initial value and applying operation from right to left to each element with its index in the original array and current accumulator value.

```kotlin
inline fun <T, R> Array<out T>.foldRightIndexed(initial: R, operation: (index: Int, T, acc: R) -> R): R(source)
```

```kotlin
fun main() {
    val items = arrayOf("apple", "banana", "cherry")

    val result = items.foldRightIndexed("") { index, item, acc ->
        "$item-$index$acc"
    }

    println(result)   // prints: cherry-2apple-1banana-0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/fold-right-indexed.html)

    