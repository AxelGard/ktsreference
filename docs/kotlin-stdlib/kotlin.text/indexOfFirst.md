

# indexOfFirst

Returns index of the first character matching the given predicate, or -1 if the char sequence does not contain such character.

```kotlin
inline fun CharSequence.indexOfFirst(predicate: (Char) -> Boolean): Int(source)
```

```kotlin
val text = "kotlin123example"
val firstDigitIndex = text.indexOfFirst { it.isDigit() }
println(firstDigitIndex)  // Output: 6
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/index-of-first.html)

    