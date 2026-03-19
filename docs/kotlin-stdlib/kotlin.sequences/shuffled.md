

# shuffled

Returns a sequence that yields elements of this sequence randomly shuffled.

```kotlin
fun <T> Sequence<T>.shuffled(): Sequence<T>(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 4, 5)
    val shuffledNumbers = numbers.shuffled()

    // Convert the shuffled sequence to a list and print it
    println(shuffledNumbers.toList())
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/shuffled.html)

    