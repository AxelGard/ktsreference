

# maxOrNull

Returns the largest element or null if the sequence is empty.

```kotlin
fun Sequence<Double>.maxOrNull(): Double?(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1.5, 3.2, 7.8, 2.9)
    val maxValue = numbers.maxOrNull()
    println("Maximum value: $maxValue")   // Output: Maximum value: 7.8
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/max-or-null.html)

    