

# reduceIndexed

Accumulates value starting with the first element and applying operation from left to right to current accumulator value and each element with its index in the original sequence.

```kotlin
inline fun <S, T : S> Sequence<T>.reduceIndexed(operation: (index: Int, acc: S, T) -> S): S(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4)

val result = numbers.reduceIndexed { index, acc, element ->
    // start with the first element, then add each element multiplied by its index
    acc + element * index
}

println(result)   // prints 21
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/reduce-indexed.html)

    