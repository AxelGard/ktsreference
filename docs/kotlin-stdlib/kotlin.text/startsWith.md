

# startsWith

Returns true if this char sequence starts with the specified character.

```kotlin
fun CharSequence.startsWith(char: Char, ignoreCase: Boolean = false): Boolean(source)
```

```kotlin
val text = "Hello, World!"

// Check if the string starts with 'H'
val startsWithH = text.startsWith('H')
println(startsWithH)          // true

// Check if the string starts with 'h', ignoring case
val startsWithHIgnoreCase = text.startsWith('h', ignoreCase = true)
println(startsWithHIgnoreCase) // true
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/starts-with.html)

    