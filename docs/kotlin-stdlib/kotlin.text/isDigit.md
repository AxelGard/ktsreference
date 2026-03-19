

# isDigit

Returns true if this character is a digit.

```kotlin
expect fun Char.isDigit(): Boolean(source)
```

```kotlin
fun main() {
    val char: Char = '5'

    if (char.isDigit()) {
        println("$char is a digit.")
    } else {
        println("$char is not a digit.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-digit.html)

    