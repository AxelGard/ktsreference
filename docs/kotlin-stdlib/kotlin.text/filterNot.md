

# filterNot

Returns a char sequence containing only those characters from the original char sequence that do not match the given predicate.

```kotlin
inline fun CharSequence.filterNot(predicate: (Char) -> Boolean): CharSequence(source)
```

```kotlin
val original = "Kotlin is fun!"
val withoutVowels = original.filterNot { it.lowercaseChar() in "aeiou" }
println(withoutVowels)  // Prints: Ktl n s fn!
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/filter-not.html)

    