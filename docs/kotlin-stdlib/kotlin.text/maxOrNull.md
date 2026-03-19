

# maxOrNull

Returns the largest character or null if the char sequence is empty.

```kotlin
fun CharSequence.maxOrNull(): Char?(source)
```

```kotlin
fun main() {
    val text = "Kotlin"
    val maxChar = text.maxOrNull()
    println("Largest char in \"$text\" is $maxChar")

    val empty = ""
    println("Largest char in empty string is ${empty.maxOrNull()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/max-or-null.html)

    