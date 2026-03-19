

# lastOrNull

Returns the last element, or null if the sequence is empty.

```kotlin
fun <T> Sequence<T>.lastOrNull(): T?(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 4, 5)
    val lastNumber = numbers.lastOrNull()
    println(lastNumber) // prints 5

    val empty = emptySequence<Int>()
    val lastEmpty = empty.lastOrNull()
    println(lastEmpty) // prints null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/last-or-null.html)

    