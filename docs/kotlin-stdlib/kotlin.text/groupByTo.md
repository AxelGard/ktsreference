

# groupByTo

Groups characters of the original char sequence by the key returned by the given keySelector function applied to each character and puts to the destination map each group key associated with a list of corresponding characters.

```kotlin
@IgnorableReturnValueinline fun <K, M : MutableMap<in K, MutableList<Char>>> CharSequence.groupByTo(destination: M, keySelector: (Char) -> K): M(source)
```

```kotlin
val text = "aabbc"
val groups = mutableMapOf<Char, MutableList<Char>>()
text.groupByTo(groups) { it }
println(groups)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/group-by-to.html)

    