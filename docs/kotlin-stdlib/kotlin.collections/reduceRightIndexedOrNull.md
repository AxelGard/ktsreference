

# reduceRightIndexedOrNull

Accumulates value starting with the last element and applying operation from right to left to each element with its index in the original array and current accumulator value.

```kotlin
inline fun <S, T : S> Array<out T>.reduceRightIndexedOrNull(operation: (index: Int, T, acc: S) -> S): S?(source)
```

```kotlin
val fruits = arrayOf("Apple", "Banana", "Cherry")
val result = fruits.reduceRightIndexedOrNull { index, fruit, acc ->
    "$fruit($index) -> $acc"
}
println(result)   // Prints: Apple(0) -> Banana(1) -> Cherry(2)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reduce-right-indexed-or-null.html)

    