

# reduceOrNull

Accumulates value starting with the first element and applying operation from left to right to current accumulator value and each element.

```kotlin
inline fun <S, T : S> Sequence<T>.reduceOrNull(operation: (acc: S, T) -> S): S?(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4)
val sum = numbers.reduceOrNull { acc, i -> acc + i }   // sum == 10

val empty = emptySequence<Int>()
val result = empty.reduceOrNull { acc, i -> acc + i }   // result == null
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/reduce-or-null.html)

    