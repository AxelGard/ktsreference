

# filterIndexed

Returns a char sequence containing only those characters from the original char sequence that match the given predicate.

```kotlin
inline fun CharSequence.filterIndexed(predicate: (index: Int, Char) -> Boolean): CharSequence(source)
```

```kotlin
val original = "kotlin"
val filtered = original.filterIndexed { index, c -> index % 2 == 0 }
println(filtered) // outputs: "koi"
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/filter-indexed.html)

    