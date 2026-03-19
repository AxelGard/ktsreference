

# lowercase

Converts this character to lower case using Unicode mapping rules of the invariant locale.

```kotlin
expect fun Char.lowercase(): String(source)
```

fun main() {
    val upper = 'A'
    val lowerStr = upper.lowercase()
    println(lowerStr) // prints "a"

    val german = 'Ü'
    println(german.lowercase()) // prints "ü"
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/lowercase.html)

    