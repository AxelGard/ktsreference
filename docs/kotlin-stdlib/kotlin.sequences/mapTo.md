

# mapTo

Applies the given transform function to each element of the original sequence and appends the results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, R, C : MutableCollection<in R>> Sequence<T>.mapTo(destination: C, transform: (T) -> R): C(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 4)
    val squares = mutableListOf<Int>()

    numbers.mapTo(squares) { it * it }

    println(squares) // prints: [1, 4, 9, 16]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/map-to.html)

    