

# reduceIndexed

Accumulates value starting with the first element and applying operation from left to right to current accumulator value and each element with its index in the original array.

```kotlin
inline fun <S, T : S> Array<out T>.reduceIndexed(operation: (index: Int, acc: S, T) -> S): S(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(2, 3, 4, 5)

    // Sum each element multiplied by its index
    val result = numbers.reduceIndexed { index, acc, value ->
        acc + index * value
    }

    println("Result: $result") // Output: Result: 26
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reduce-indexed.html)

    