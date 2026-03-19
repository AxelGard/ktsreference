

# takeWhile

Returns a sequence containing first elements satisfying the given predicate.

```kotlin
fun <T> Sequence<T>.takeWhile(predicate: (T) -> Boolean): Sequence<T>(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5, 6)
val firstThree = numbers.takeWhile { it < 4 }.toList()

println(firstThree)  // prints: [1, 2, 3]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/take-while.html)

    