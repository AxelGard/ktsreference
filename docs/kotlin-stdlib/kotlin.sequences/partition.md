

# partition

Splits the original sequence into a pair of lists, where first list contains elements for which predicate yielded true, while second list contains elements for which predicate yielded false.

```kotlin
inline fun <T> Sequence<T>.partition(predicate: (T) -> Boolean): Pair<List<T>, List<T>>(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5, 6)

val (evens, odds) = numbers.partition { it % 2 == 0 }

println("Even numbers: $evens")  // [2, 4, 6]
println("Odd numbers: $odds")    // [1, 3, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/partition.html)

    