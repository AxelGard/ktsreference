

# findLast

Returns the last character matching the given predicate, or null if no such character was found.

```kotlin
inline fun CharSequence.findLast(predicate: (Char) -> Boolean): Char?(source)
```

```kotlin
val text = "Kotlin1234"
val lastDigit: Char? = text.findLast { it.isDigit() }  // lastDigit == '4'
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/find-last.html)

    