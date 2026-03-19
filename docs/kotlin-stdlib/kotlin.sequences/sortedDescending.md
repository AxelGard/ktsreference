

# sortedDescending

Returns a sequence that yields elements of this sequence sorted descending according to their natural sort order.

```kotlin
fun <T : Comparable<T>> Sequence<T>.sortedDescending(): Sequence<T>(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(10, 2, 8, 4, 6)
    val descending = numbers.sortedDescending()
    println(descending.toList()) // [10, 8, 6, 4, 2]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sorted-descending.html)

    