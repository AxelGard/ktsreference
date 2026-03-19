

# dropLast

Returns a subsequence of this char sequence with the last n characters removed.

```kotlin
fun CharSequence.dropLast(n: Int): CharSequence(source)
```

```kotlin
val text = "Hello, World!"
val shortened = text.dropLast(6)   // "Hello, "
println(shortened)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/drop-last.html)

    