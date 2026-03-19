

# reduceTo

Groups elements from the Grouping source by key and applies the reducing operation to the elements of each group sequentially starting from the second element of the group, passing the previously accumulated value and the current element as arguments, and stores the results in the given destination map. An initial value of accumulator is the first element of the group.

```kotlin
inline fun <S, T : S, K, M : MutableMap<in K, S>> Grouping<T, K>.reduceTo(destination: M, operation: (key: K, accumulator: S, element: T) -> S): M(source)
```

```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6, 7, 8)

val maxPerParity = numbers
    .groupingBy { it % 2 }                    // group by 0 (even) or 1 (odd)
    .reduceTo(mutableMapOf<Int, Int>()) { key, acc, element ->
        maxOf(acc, element)                  // keep the largest number in each group
    }

println(maxPerParity)   // prints: {0=8, 1=7}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reduce-to.html)

    