

# sorted

Returns a sequence that yields elements of this sequence sorted according to their natural sort order.

```kotlin
fun <T : Comparable<T>> Sequence<T>.sorted(): Sequence<T>(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(3, 1, 4, 1, 5, 9)
    val sortedNumbers = numbers.sorted()
    println(sortedNumbers.toList()) // Output: [1, 1, 3, 4, 5, 9]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sorted.html)

    