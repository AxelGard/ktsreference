

# isLetter

Returns true if this character is a letter.

```kotlin
expect fun Char.isLetter(): Boolean(source)
```

```kotlin
fun main() {
    val chars = listOf('a', '1', 'ß', ' ', '\n')

    for (c in chars) {
        if (c.isLetter()) {
            println("'$c' is a letter")
        } else {
            println("'$c' is not a letter")
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-letter.html)

    