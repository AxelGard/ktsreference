

# find

Returns the first element matching the given predicate, or null if no such element was found.

```kotlin
inline fun <T> Array<out T>.find(predicate: (T) -> Boolean): T?(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4, 5)
val result = numbers.find { it > 3 }
println(result)   // Prints: 4
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/find.html)

    