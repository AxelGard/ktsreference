

# firstOrNull

Returns the first character, or null if the char sequence is empty.

```kotlin
fun CharSequence.firstOrNull(): Char?(source)
```

```kotlin
fun main() {
    val text = "Hello, world!"
    val firstChar = text.firstOrNull()
    println(firstChar)          // Prints: H

    val emptyText = ""
    val noChar = emptyText.firstOrNull()
    println(noChar)             // Prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/first-or-null.html)

    