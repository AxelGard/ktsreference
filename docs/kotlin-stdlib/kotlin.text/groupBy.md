

# groupBy

Groups characters of the original char sequence by the key returned by the given keySelector function applied to each character and returns a map where each group key is associated with a list of corresponding characters.

```kotlin
inline fun <K> CharSequence.groupBy(keySelector: (Char) -> K): Map<K, List<Char>>(source)
```

```kotlin
val text = "banana"
val grouped = text.groupBy { it }
println(grouped) // {b=[b], a=[a, a, a], n=[n, n]}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/group-by.html)

    