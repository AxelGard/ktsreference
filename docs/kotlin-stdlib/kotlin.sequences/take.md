

# take

Returns a sequence containing first n elements.

```kotlin
fun <T> Sequence<T>.take(n: Int): Sequence<T>(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5)

numbers
    .take(3)          // keep only the first 3 elements
    .forEach { println(it) }   // prints: 1 2 3
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/take.html)

    