

# firstOrNull

Returns the first element, or null if the sequence is empty.

```kotlin
fun <T> Sequence<T>.firstOrNull(): T?(source)
```

```kotlin
fun main() {
    val seq = sequenceOf("apple", "banana", "cherry")
    val first = seq.firstOrNull()
    println(first)          // prints "apple"

    val emptySeq = emptySequence<String>()
    val firstEmpty = emptySeq.firstOrNull()
    println(firstEmpty)     // prints "null"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/first-or-null.html)

    