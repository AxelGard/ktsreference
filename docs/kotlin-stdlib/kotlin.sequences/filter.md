

# filter

Returns a sequence containing only elements matching the given predicate.

```kotlin
fun <T> Sequence<T>.filter(predicate: (T) -> Boolean): Sequence<T>(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5, 6)

val evens = numbers.filter { it % 2 == 0 }

println(evens.toList())  // Output: [2, 4, 6]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/filter.html)

    