

# minOfWith

Returns the smallest value according to the provided comparator among all values produced by selector function applied to each element in the array.

```kotlin
inline fun <T, R> Array<out T>.minOfWith(comparator: Comparator<in R>, selector: (T) -> R): R(source)
```

```kotlin
val words = arrayOf("apple", "banana", "cherry", "date")

val shortest = words.minOfWith(compareBy<String> { it.length }) { it }

println(shortest)   // prints: date
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min-of-with.html)

    