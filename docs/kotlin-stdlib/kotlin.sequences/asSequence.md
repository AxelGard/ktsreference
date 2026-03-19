

# asSequence

Returns this sequence as a Sequence.

```kotlin
inline fun <T> Sequence<T>.asSequence(): Sequence<T>(source)
```

```kotlin
val numbers = listOf(1, 2, 3, 4, 5)

val doubledEven = numbers.asSequence()
    .filter { it % 2 == 0 }
    .map { it * 2 }
    .toList()

println(doubledEven)  // prints: [4, 8]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/as-sequence.html)

    