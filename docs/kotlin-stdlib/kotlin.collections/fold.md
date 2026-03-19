

# fold

Accumulates value starting with initial value and applying operation from left to right to current accumulator value and each element.

```kotlin
inline fun <T, R> Array<out T>.fold(initial: R, operation: (acc: R, T) -> R): R(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4, 5)
val sum = numbers.fold(0) { acc, value -> acc + value }
println("Sum: $sum")  // Output: Sum: 15
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/fold.html)

    