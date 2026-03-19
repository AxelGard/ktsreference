

# findAnyOf

Finds the first occurrence of any of the specified strings in this char sequence, starting from the specified startIndex and optionally ignoring the case.

```kotlin
fun CharSequence.findAnyOf(strings: Collection<String>, startIndex: Int = 0, ignoreCase: Boolean = false): Pair<Int, String>?(source)
```

```kotlin
fun main() {
    val text = "Kotlin is great, but Java is also popular."
    val patterns = listOf("great", "Java", "Python")

    // Find the first occurrence of any pattern, starting after index 5, ignoring case
    val match: Pair<Int, String>? = text.findAnyOf(patterns, startIndex = 5, ignoreCase = true)

    println(match)  // e.g., prints: (9, "great")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/find-any-of.html)

    