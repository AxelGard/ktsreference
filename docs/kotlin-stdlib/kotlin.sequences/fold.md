

# fold

Accumulates value starting with initial value and applying operation from left to right to current accumulator value and each element.

```kotlin
inline fun <T, R> Sequence<T>.fold(initial: R, operation: (acc: R, T) -> R): R(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 4, 5)
    val sum = numbers.fold(0) { acc, number -> acc + number }
    println("Sum: $sum") // Sum: 15
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/fold.html)

    