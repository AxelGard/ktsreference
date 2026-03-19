

# any

Returns true if sequence has at least one element.

```kotlin
fun <T> Sequence<T>.any(): Boolean(source)
```

```kotlin
fun main() {
    // Sequence with elements
    val numbers = sequenceOf(10, 20, 30)
    println(numbers.any())          // → true

    // Empty sequence
    val empty = emptySequence<Int>()
    println(empty.any())            // → false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/any.html)

    