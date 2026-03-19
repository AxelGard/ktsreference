

# reduceIndexedOrNull

Accumulates value starting with the first element and applying operation from left to right to current accumulator value and each element with its index in the original sequence.

```kotlin
inline fun <S, T : S> Sequence<T>.reduceIndexedOrNull(operation: (index: Int, acc: S, T) -> S): S?(source)
```

```kotlin
fun main() {
    // Non‑empty sequence: weighted sum = 0*10 + 1*20 + 2*30 = 80
    val weightedSum = listOf(10, 20, 30).asSequence()
        .reduceIndexedOrNull { index, acc, value -> acc + value * index }

    println(weightedSum)   // prints: 80

    // Empty sequence: returns null
    val emptySum = emptySequence<Int>()
        .reduceIndexedOrNull { index, acc, value -> acc + value * index }

    println(emptySum)      // prints: null
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/reduce-indexed-or-null.html)

    