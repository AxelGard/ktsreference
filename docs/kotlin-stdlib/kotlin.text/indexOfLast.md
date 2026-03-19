

# indexOfLast

Returns index of the last character matching the given predicate, or -1 if the char sequence does not contain such character.

```kotlin
inline fun CharSequence.indexOfLast(predicate: (Char) -> Boolean): Int(source)
```

```kotlin
fun main() {
    val text = "Hello Kotlin, Welcome to Kotlin!"

    // Find the index of the last uppercase letter
    val lastUppercaseIndex = text.indexOfLast { it.isUpperCase() }
    println("Last uppercase letter is at index: $lastUppercaseIndex")

    // Find the index of the last vowel
    val lastVowelIndex = text.indexOfLast { it.lowercaseChar() in "aeiou" }
    println("Last vowel is at index: $lastVowelIndex")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/index-of-last.html)

    