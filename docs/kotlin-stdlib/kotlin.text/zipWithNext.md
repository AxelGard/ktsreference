

# zipWithNext

Returns a list of pairs of each two adjacent characters in this char sequence.

```kotlin
fun CharSequence.zipWithNext(): List<Pair<Char, Char>>(source)
```

```kotlin
fun main() {
    val text = "hello"

    val pairs = text.zipWithNext()          // ["h" to "e", "e" to "l", "l" to "l", "l" to "o"]
    println(pairs)

    // Iterate over the pairs
    pairs.forEach { (first, second) ->
        println("$first -> $second")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/zip-with-next.html)

    