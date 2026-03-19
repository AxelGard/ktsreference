

# reduce

Accumulates value starting with the first element and applying operation from left to right to current accumulator value and each element.

```kotlin
inline fun <S, T : S> Sequence<T>.reduce(operation: (acc: S, T) -> S): S(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5)
val sum = numbers.reduce { acc, n -> acc + n }
println(sum)  // Output: 15
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/reduce.html)

    