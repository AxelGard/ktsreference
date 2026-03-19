

# reduceOrNull

Accumulates value starting with the first element and applying operation from left to right to current accumulator value and each element.

```kotlin
inline fun <S, T : S> Array<out T>.reduceOrNull(operation: (acc: S, T) -> S): S?(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4, 5)
val sum = numbers.reduceOrNull { acc, n -> acc + n }
println(sum)   // prints 15
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reduce-or-null.html)

    