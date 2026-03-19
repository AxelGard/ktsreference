

# associate

Returns a Map containing key-value pairs provided by transform function applied to characters of the given char sequence.

```kotlin
inline fun <K, V> CharSequence.associate(transform: (Char) -> Pair<K, V>): Map<K, V>(source)
```

```kotlin
fun main() {
    val text = "kotlin"

    // Create a map that associates each character with its ASCII code
    val asciiMap: Map<Char, Int> = text.associate { ch ->
        ch to ch.code   // Pair<Char, Int>
    }

    println(asciiMap)   // Output: {k=107, o=111, t=116, l=108, i=105, n=110}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/associate.html)

    