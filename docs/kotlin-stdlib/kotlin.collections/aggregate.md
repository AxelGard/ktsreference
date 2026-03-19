

# aggregate

Groups elements from the Grouping source by key and applies operation to the elements of each group sequentially, passing the previously accumulated value and the current element as arguments, and stores the results in a new map.

```kotlin
inline fun <T, K, R> Grouping<T, K>.aggregate(operation: (key: K, accumulator: R?, element: T, first: Boolean) -> R): Map<K, R>(source)
```

```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)

val sumByParity: Map<Boolean, Int> = numbers.groupingBy { it % 2 == 0 }
    .aggregate { key, acc, element, first ->
        // acc is null on first element of the group, otherwise it's the current sum
        (acc ?: 0) + element
    }

println(sumByParity)   // Output: {false=9, true=12}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/aggregate.html)

    