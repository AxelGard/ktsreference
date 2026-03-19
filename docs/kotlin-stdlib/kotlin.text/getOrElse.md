

# getOrElse

Returns a character at the given index or the result of calling the defaultValue function if the index is out of bounds of this char sequence.

```kotlin
inline fun CharSequence.getOrElse(index: Int, defaultValue: (Int) -> Char): Char(source)
```

```kotlin
val text = "Kotlin"

val charAtIndex = text.getOrElse(10) { index ->
    // If index is out of bounds, return a placeholder character
    // Here we cycle through the alphabet starting from 'A'
    ('A' + index % 26)
}

println("Character: $charAtIndex")  // Prints: Character: K
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/get-or-else.html)

    