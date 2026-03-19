

# foldIndexed

Accumulates value starting with initial value and applying operation from left to right to current accumulator value and each element with its index in the original array.

```kotlin
inline fun <T, R> Array<out T>.foldIndexed(initial: R, operation: (index: Int, acc: R, T) -> R): R(source)
```

```kotlin
val numbers = arrayOf(10, 20, 30, 40)

val result = numbers.foldIndexed(0) { index, acc, value ->
    acc + value * index
}

println(result)  // Output: 140
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/fold-indexed.html)

    