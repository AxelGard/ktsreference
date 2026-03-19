

# reduceIndexedOrNull

Accumulates value starting with the first element and applying operation from left to right to current accumulator value and each element with its index in the original array.

```kotlin
inline fun <S, T : S> Array<out T>.reduceIndexedOrNull(operation: (index: Int, acc: S, T) -> S): S?(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4)

// Sum the elements (works even with the index if needed)
val sum = numbers.reduceIndexedOrNull { index, acc, value -> acc + value }
println(sum)          // 10

// When the array is empty, the result is null
val empty = emptyArray<Int>()
val emptyResult = empty.reduceIndexedOrNull { index, acc, value -> acc + value }
println(emptyResult)  // null
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reduce-indexed-or-null.html)

    