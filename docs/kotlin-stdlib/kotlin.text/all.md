

# all

Returns true if all characters match the given predicate.

```kotlin
inline fun CharSequence.all(predicate: (Char) -> Boolean): Boolean(source)
```

```kotlin
fun main() {
    val text = "kotlin"
    val allLetters = text.all { it.isLetter() }
    println("All characters are letters: $allLetters")   // prints: All characters are letters: true

    val numbers = "12345"
    val allDigits = numbers.all { it.isDigit() }
    println("All characters are digits: $allDigits")     // prints: All characters are digits: true

    val mixed = "k3a"
    val allLettersMixed = mixed.all { it.isLetter() }
    println("All characters are letters: $allLettersMixed") // prints: All characters are letters: false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/all.html)

    