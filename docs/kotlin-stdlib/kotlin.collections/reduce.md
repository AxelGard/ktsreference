

# reduce

Accumulates value starting with the first element and applying operation from left to right to current accumulator value and each element.

```kotlin
inline fun <S, T : S> Array<out T>.reduce(operation: (acc: S, T) -> S): S(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 4)
    val sum = numbers.reduce { acc, n -> acc + n }
    println("Sum: $sum")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reduce.html)

    