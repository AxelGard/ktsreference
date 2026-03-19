

# chunked

Splits this collection into a list of lists each not exceeding the given size.

```kotlin
fun <T> Iterable<T>.chunked(size: Int): List<List<T>>(source)
```

```kotlin
fun main() {
    val items = listOf("a", "b", "c", "d", "e", "f", "g")
    val chunked = items.chunked(3)

    chunked.forEachIndexed { index, chunk ->
        println("Chunk ${index + 1}: $chunk")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/chunked.html)

    