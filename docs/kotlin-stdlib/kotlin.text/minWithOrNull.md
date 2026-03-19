

# minWithOrNull

Returns the first character having the smallest value according to the provided comparator or null if there are no characters.

```kotlin
fun CharSequence.minWithOrNull(comparator: Comparator<in Char>): Char?(source)
```

```kotlin
fun main() {
    val text = "kotlin"

    // Comparator that orders characters in natural order
    val comp = Comparator<Char> { c1, c2 -> c1.compareTo(c2) }

    // Finds the smallest character according to the comparator
    val minChar = text.minWithOrNull(comp)
    println(minChar)  // prints: k

    // Empty string – no characters to compare
    val empty = ""
    val none = empty.minWithOrNull(comp)
    println(none)     // prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/min-with-or-null.html)

    