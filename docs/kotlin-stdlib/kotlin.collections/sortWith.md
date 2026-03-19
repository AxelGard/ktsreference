

# sortWith

Sorts the array in-place according to the order specified by the given comparator.

```kotlin
expect fun <T> Array<out T>.sortWith(comparator: Comparator<in T>)(source)
```

```kotlin
val numbers = arrayOf(4, 2, 7, 1, 5)

val ascending = Comparator<Int> { a, b -> a - b }
numbers.sortWith(ascending)

println(numbers.contentToString())  // [1, 2, 4, 5, 7]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sort-with.html)

    