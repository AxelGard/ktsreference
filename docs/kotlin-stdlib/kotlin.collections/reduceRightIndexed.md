

# reduceRightIndexed

Accumulates value starting with the last element and applying operation from right to left to each element with its index in the original array and current accumulator value.

```kotlin
inline fun <S, T : S> Array<out T>.reduceRightIndexed(operation: (index: Int, T, acc: S) -> S): S(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4, 5)

val result = numbers.reduceRightIndexed { index, value, acc ->
    // Accumulate a sum of value multiplied by its index
    acc + value * index
}

println(result)   // prints 45
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reduce-right-indexed.html)

    