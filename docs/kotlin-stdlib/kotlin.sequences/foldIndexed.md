

# foldIndexed

Accumulates value starting with initial value and applying operation from left to right to current accumulator value and each element with its index in the original sequence.

```kotlin
inline fun <T, R> Sequence<T>.foldIndexed(initial: R, operation: (index: Int, acc: R, T) -> R): R(source)
```

```kotlin
val numbers = sequenceOf(10, 20, 30)

val weightedSum = numbers.foldIndexed(0) { index, acc, value ->
    acc + value * (index + 1)   // weight by position (1‑based)
}

println("Weighted sum: $weightedSum")   // prints: Weighted sum: 140
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/fold-indexed.html)

    