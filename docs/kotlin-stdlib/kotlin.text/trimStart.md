

# trimStart

Returns a subsequence of this char sequence having leading characters matching the predicate removed.

```kotlin
inline fun CharSequence.trimStart(predicate: (Char) -> Boolean): CharSequence(source)
```

```kotlin
val input = "12345Hello World"
val trimmed = input.trimStart { it.isDigit() }
println(trimmed)   // Output: Hello World
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim-start.html)

    