

# lowercaseChar

Converts this character to lower case using Unicode mapping rules of the invariant locale.

```kotlin
expect fun Char.lowercaseChar(): Char(source)
```

```kotlin
fun main() {
    val upper: Char = 'A'
    val lower = upper.lowercaseChar()
    println("Lowercase of $upper is $lower")  // prints: Lowercase of A is a
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/lowercase-char.html)

    