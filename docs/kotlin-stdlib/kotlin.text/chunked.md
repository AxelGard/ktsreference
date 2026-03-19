

# chunked

Splits this char sequence into a list of strings each not exceeding the given size.

```kotlin
fun CharSequence.chunked(size: Int): List<String>(source)
```

```kotlin
val text = "abcdefghijklmnopqrstuvwxyz"
val chunks = text.chunked(5)
println(chunks) // [abcde, fghij, klmno, pqrst, uvwxy, z]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/chunked.html)

    