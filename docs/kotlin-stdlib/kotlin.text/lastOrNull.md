

# lastOrNull

Returns the last character, or null if the char sequence is empty.

```kotlin
fun CharSequence.lastOrNull(): Char?(source)
```

```kotlin
fun main() {
    val text = "Kotlin"
    val lastChar: Char? = text.lastOrNull()
    println(lastChar) // prints 'n'

    val empty = ""
    val lastEmpty: Char? = empty.lastOrNull()
    println(lastEmpty) // prints 'null'
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/last-or-null.html)

    