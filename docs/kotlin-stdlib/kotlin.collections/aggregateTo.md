

# aggregateTo

Groups elements from the Grouping source by key and applies operation to the elements of each group sequentially, passing the previously accumulated value and the current element as arguments, and stores the results in the given destination map.

```kotlin
inline fun <T, K, R, M : MutableMap<in K, R>> Grouping<T, K>.aggregateTo(destination: M, operation: (key: K, accumulator: R?, element: T, first: Boolean) -> R): M(source)
```

```kotlin
val words = listOf("apple", "apricot", "banana", "blueberry", "cherry")

val result = words.groupingBy { it.first() }
    .aggregateTo(mutableMapOf()) { key, acc, element, first ->
        val len = element.length
        if (first) len else acc!! + len
    }

println(result)  // {a=12, b=20, c=6}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/aggregate-to.html)

    