

# intersect

Returns a set containing elements of this array that are also contained in the specified other array.

```kotlin
infix fun <T> Array<out T>.intersect(other: Iterable<T>): Set<T>(source)
```

```kotlin
val fruits = arrayOf("apple", "banana", "cherry", "date")
val favorites = listOf("banana", "date", "fig", "grape")

val common = fruits intersect favorites

println(common)   // Output: [banana, date]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/intersect.html)

    