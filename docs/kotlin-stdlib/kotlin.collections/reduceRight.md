

# reduceRight

Accumulates value starting with the last element and applying operation from right to left to each element and current accumulator value.

```kotlin
inline fun <S, T : S> Array<out T>.reduceRight(operation: (T, acc: S) -> S): S(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4)

val product = numbers.reduceRight { a, acc -> a * acc }

println(product)   // 24
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reduce-right.html)

    