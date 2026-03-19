

# flatMapIndexed

Returns a single list of all elements yielded from results of transform function being invoked on each character and its index in the original char sequence.

```kotlin
@JvmName(name = "flatMapIndexedIterable")inline fun <R> CharSequence.flatMapIndexed(transform: (index: Int, Char) -> Iterable<R>): List<R>(source)
```

```kotlin
fun main() {
    val input = "abc"
    val result = input.flatMapIndexed { index, char ->
        listOf(char, index.toString())
    }
    println(result)  // [a, 0, b, 1, c, 2]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/flat-map-indexed.html)

    