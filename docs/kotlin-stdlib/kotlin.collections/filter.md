

# filter

Returns a list containing only elements matching the given predicate.

```kotlin
inline fun <T> Array<out T>.filter(predicate: (T) -> Boolean): List<T>(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4, 5, 6)
val evens = numbers.filter { it % 2 == 0 }
println(evens)   // Output: [2, 4, 6]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter.html)

    