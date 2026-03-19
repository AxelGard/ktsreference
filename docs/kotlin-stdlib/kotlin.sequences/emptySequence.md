

# emptySequence

Returns an empty sequence.

```kotlin
fun <T> emptySequence(): Sequence<T>(source)
```

```kotlin
fun main() {
    // Create an empty sequence of Int
    val empty: Sequence<Int> = emptySequence()

    // Operations on the empty sequence have no effect
    val result = empty
        .map { it * 2 }          // no elements, nothing to map
        .filter { it > 10 }      // no elements, nothing to filter

    // The resulting sequence is still empty
    println(result.toList())    // prints []
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/empty-sequence.html)

    