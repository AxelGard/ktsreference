

# chunked

Splits this sequence into a sequence of lists each not exceeding the given size.

```kotlin
fun <T> Sequence<T>.chunked(size: Int): Sequence<List<T>>(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    val result = numbers.chunked(3).toList()
    println(result)   // [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/chunked.html)

    