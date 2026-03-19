

# mapNotNull

Returns a sequence containing only the non-null results of applying the given transform function to each element in the original sequence.

```kotlin
fun <T, R : Any> Sequence<T>.mapNotNull(transform: (T) -> R?): Sequence<R>(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 4, 5)

    val evenHalves = numbers.mapNotNull { if (it % 2 == 0) it / 2 else null }

    println(evenHalves.toList())   // Output: [1, 2]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/map-not-null.html)

    