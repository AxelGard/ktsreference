

# toHashSet

Returns a new HashSet of all elements.

```kotlin
fun <T> Sequence<T>.toHashSet(): HashSet<T>(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 2, 4, 3)
    val uniqueNumbers = numbers.toHashSet()
    println(uniqueNumbers)   // Output: [1, 2, 3, 4]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/to-hash-set.html)

    