

# maxWithOrNull

Returns the first character having the largest value according to the provided comparator or null if there are no characters.

```kotlin
fun CharSequence.maxWithOrNull(comparator: Comparator<in Char>): Char?(source)
```

```kotlin
fun main() {
    val text = "Kotlin"
    // Find the character with the highest natural order value
    val maxChar = text.maxWithOrNull(compareBy<Char> { it })
    println(maxChar)   // prints: t

    // Example with an empty string – result is null
    val empty = "".maxWithOrNull(compareBy<Char> { it })
    println(empty)     // prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/max-with-or-null.html)

    