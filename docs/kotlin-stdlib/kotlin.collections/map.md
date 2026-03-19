

# map

Returns a list containing the results of applying the given transform function to each element in the original array.

```kotlin
inline fun <T, R> Array<out T>.map(transform: (T) -> R): List<R>(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4)
val squares = numbers.map { it * it }
println(squares) // prints [1, 4, 9, 16]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map.html)

    