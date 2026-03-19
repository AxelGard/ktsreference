

# onEach

Returns a sequence which performs the given action on each element of the original sequence as they pass through it.

```kotlin
fun <T> Sequence<T>.onEach(action: (T) -> Unit): Sequence<T>(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 4, 5)

    val result = numbers
        .onEach { println("Processing number: $it") }   // side‑effect
        .map { it * 2 }                                 // transformation
        .toList()                                       // terminal operation

    println("Result: $result")   // Output: Result: [2, 4, 6, 8, 10]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/on-each.html)

    