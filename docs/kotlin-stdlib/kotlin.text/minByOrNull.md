

# minByOrNull

Returns the first character yielding the smallest value of the given selector function or null if there are no characters.

```kotlin
inline fun <R : Comparable<R>> CharSequence.minByOrNull(selector: (Char) -> R): Char?(source)
```

```kotlin
val text = "Kotlin is awesome!"

// Find the first lowercase character (smallest by the selector)
val firstLowercase = text.minByOrNull { if (it.isLowerCase()) 0 else 1 }

println(firstLowercase)  // Output: o
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/min-by-or-null.html)

    