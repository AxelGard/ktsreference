

# toSet

Returns a Set of all elements.

```kotlin
fun <T> Sequence<T>.toSet(): Set<T>(source)
```

```kotlin
fun main() {
    // Create a sequence with duplicate values
    val seq = sequenceOf("apple", "banana", "apple", "orange")

    // Convert the sequence to a set, removing duplicates
    val set = seq.toSet()

    // Print the resulting set
    println(set)   // Output: [apple, banana, orange]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/to-set.html)

    