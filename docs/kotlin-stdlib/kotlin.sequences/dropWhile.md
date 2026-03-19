

# dropWhile

Returns a sequence containing all elements except first elements that satisfy the given predicate.

```kotlin
fun <T> Sequence<T>.dropWhile(predicate: (T) -> Boolean): Sequence<T>(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5)
val dropped = numbers.dropWhile { it < 3 }.toList()
println(dropped) // Output: [3, 4, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/drop-while.html)

    