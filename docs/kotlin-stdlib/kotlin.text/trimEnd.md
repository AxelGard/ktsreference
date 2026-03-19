

# trimEnd

Returns a subsequence of this char sequence having trailing characters matching the predicate removed.

```kotlin
inline fun CharSequence.trimEnd(predicate: (Char) -> Boolean): CharSequence(source)
```

```kotlin
val text = "Hello, world!!!"
val trimmed = text.trimEnd { it == '!' }
println(trimmed)   // prints: Hello, world
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim-end.html)

    