

# map

Returns a sequence containing the results of applying the given transform function to each element in the original sequence.

```kotlin
fun <T, R> Sequence<T>.map(transform: (T) -> R): Sequence<R>(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 4)
    val squares = numbers.map { it * it }.toList()
    println(squares) // [1, 4, 9, 16]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/map.html)

    