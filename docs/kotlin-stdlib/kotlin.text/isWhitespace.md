

# isWhitespace

Determines whether a character is whitespace.

```kotlin
expect fun Char.isWhitespace(): Boolean(source)
```

```kotlin
fun main() {
    val text = "Hello, World!\n"
    for (c in text) {
        if (c.isWhitespace()) {
            println("Whitespace found: '$c'")
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-whitespace.html)

    