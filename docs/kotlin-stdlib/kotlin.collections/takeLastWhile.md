

# takeLastWhile

Returns a list containing last elements satisfying the given predicate.

```kotlin
inline fun <T> Array<out T>.takeLastWhile(predicate: (T) -> Boolean): List<T>(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4, 5, 6)
val lastGreaterThanThree = numbers.takeLastWhile { it > 3 }
println(lastGreaterThanThree) // [4, 5, 6]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/take-last-while.html)

    