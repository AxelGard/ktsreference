

# subtract

Returns a set containing all elements that are contained by this array and not contained by the specified collection.

```kotlin
infix fun <T> Array<out T>.subtract(other: Iterable<T>): Set<T>(source)
```

```kotlin
val arr = arrayOf(1, 2, 3, 4, 5)
val toRemove = listOf(2, 4)

val result: Set<Int> = arr subtract toRemove

println(result) // Output: [1, 3, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/subtract.html)

    