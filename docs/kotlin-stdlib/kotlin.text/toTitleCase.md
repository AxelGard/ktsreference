

# toTitleCase

Warning since 1.5

```kotlin
inline fun Char.toTitleCase(): Char(source)
```

```kotlin
fun main() {
    val lowerChar: Char = 'k'
    val titleChar: Char = lowerChar.toTitleCase()
    println(titleChar)          // Output: K

    // Convert a whole string to title case
    val text = "kotlin"
    val titleText = text.map { it.toTitleCase() }.joinToString("")
    println(titleText)          // Output: Kotlin
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-title-case.html)

    