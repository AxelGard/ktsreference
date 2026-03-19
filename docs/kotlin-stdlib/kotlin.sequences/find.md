

# find

Returns the first element matching the given predicate, or null if no such element was found.

```kotlin
inline fun <T> Sequence<T>.find(predicate: (T) -> Boolean): T?(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5)
val firstGreaterThanThree = numbers.find { it > 3 }
println(firstGreaterThanThree) // 4
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/find.html)

    