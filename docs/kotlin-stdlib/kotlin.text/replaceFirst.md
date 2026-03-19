

# replaceFirst

Replaces the first occurrence of the given regular expression regex in this char sequence with the specified replacement expression.

```kotlin
inline fun CharSequence.replaceFirst(regex: Regex, replacement: String): String(source)
```

```kotlin
val text = "apple banana apple"
val newText = text.replaceFirst(Regex("apple"), "orange")
println(newText)  // prints: orange banana apple
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace-first.html)

    