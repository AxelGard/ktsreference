

# asSequence

Creates a Sequence instance that wraps the original array returning its elements when being iterated.

```kotlin
fun <T> Array<out T>.asSequence(): Sequence<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5)

    val result = numbers
        .asSequence()            // Convert array to a lazy Sequence
        .filter { it % 2 == 0 }   // Keep only even numbers
        .map { it * 10 }          // Multiply each by 10
        .toList()                 // Materialize the sequence into a List

    println(result)  // Output: [20, 40]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-sequence.html)

    