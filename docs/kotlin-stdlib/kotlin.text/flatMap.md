

# flatMap

Returns a single list of all elements yielded from results of transform function being invoked on each character of original char sequence.

```kotlin
inline fun <R> CharSequence.flatMap(transform: (Char) -> Iterable<R>): List<R>(source)
```

```kotlin
fun main() {
    val input = "abc"

    // For each character produce a list of its uppercase and lowercase form
    val expanded = input.flatMap { ch ->
        listOf(ch.uppercaseChar(), ch.lowercaseChar())
    }

    println(expanded) // Output: [A, a, B, b, C, c]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/flat-map.html)

    