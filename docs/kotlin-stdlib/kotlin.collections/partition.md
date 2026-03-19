

# partition

Splits the original array into a pair of lists, where first list contains elements for which predicate yielded true, while second list contains elements for which predicate yielded false.

```kotlin
inline fun <T> Array<out T>.partition(predicate: (T) -> Boolean): Pair<List<T>, List<T>>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5, 6)
    val (evens, odds) = numbers.partition { it % 2 == 0 }

    println("Evens: $evens") // [2, 4, 6]
    println("Odds: $odds")   // [1, 3, 5]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/partition.html)

    