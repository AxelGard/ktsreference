

# filterNotTo

Appends all characters not matching the given predicate to the given destination.

```kotlin
@IgnorableReturnValueinline fun <C : Appendable> CharSequence.filterNotTo(destination: C, predicate: (Char) -> Boolean): C(source)
```

```kotlin
val text = "Kotlin is great!"
val result = StringBuilder()

// Append all characters that are NOT a space to the StringBuilder
text.filterNotTo(result) { it == ' ' }

println(result.toString())   // prints: Kotlinisgreat!
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/filter-not-to.html)

    