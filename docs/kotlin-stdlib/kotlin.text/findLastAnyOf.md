

# findLastAnyOf

Finds the last occurrence of any of the specified strings in this char sequence, starting from the specified startIndex and optionally ignoring the case.

```kotlin
fun CharSequence.findLastAnyOf(strings: Collection<String>, startIndex: Int = lastIndex, ignoreCase: Boolean = false): Pair<Int, String>?(source)
```

```kotlin
fun main() {
    val text = "The quick brown fox jumps over the lazy dog. The quick brown fox."
    val searchWords = listOf("fox", "dog", "cat")

    // Find the last occurrence of any of the search words (case‑insensitive)
    val result = text.findLastAnyOf(searchWords, ignoreCase = true)

    if (result != null) {
        val (index, matched) = result
        println("Last match at index $index: '$matched'")
    } else {
        println("No match found")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/find-last-any-of.html)

    