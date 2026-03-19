

# dropLastWhile

Returns a list containing all elements except last elements that satisfy the given predicate.

```kotlin
inline fun <T> Array<out T>.dropLastWhile(predicate: (T) -> Boolean): List<T>(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4, 5, 6)
val result = numbers.dropLastWhile { it % 2 == 0 }  // result: [1, 2, 3, 4, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/drop-last-while.html)

    