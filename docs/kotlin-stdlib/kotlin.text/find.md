

# find

Returns the first character matching the given predicate, or null if no such character was found.

```kotlin
inline fun CharSequence.find(predicate: (Char) -> Boolean): Char?(source)
```

val text = "Kotlin is great"
val firstVowel = text.find { it in "aeiouAEIOU" }
println(firstVowel) // prints 'o'

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/find.html)

    