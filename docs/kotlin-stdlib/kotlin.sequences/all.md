

# all

Returns true if all elements match the given predicate.

```kotlin
inline fun <T> Sequence<T>.all(predicate: (T) -> Boolean): Boolean(source)
```

```kotlin
val numbers = sequenceOf(2, 4, 6, 8, 10)
val allEven = numbers.all { it % 2 == 0 }

println("All numbers are even? $allEven")  // Prints: All numbers are even? true
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/all.html)

    