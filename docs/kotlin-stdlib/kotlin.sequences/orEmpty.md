

# orEmpty

Returns this sequence if it's not null and the empty sequence otherwise.

```kotlin
inline fun <T> Sequence<T>?.orEmpty(): Sequence<T>(source)
```

```kotlin
val nonNullSeq: Sequence<String>? = listOf("a", "b", "c").asSequence()
val nullSeq: Sequence<String>? = null

println("Non‑null sequence:")
nonNullSeq.orEmpty().forEach { println(it) }

println("Null sequence:")
nullSeq.orEmpty().forEach { println(it) }  // nothing printed
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/or-empty.html)

    