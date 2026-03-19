

# associateTo

Populates and returns the destination mutable map with key-value pairs provided by transform function applied to each character of the given char sequence.

```kotlin
@IgnorableReturnValueinline fun <K, V, M : MutableMap<in K, in V>> CharSequence.associateTo(destination: M, transform: (Char) -> Pair<K, V>): M(source)
```

```kotlin
val map = mutableMapOf<Char, Int>()
"kotlin".associateTo(map) { ch -> ch to ch.code }
println(map)   // e.g., {k=107, o=111, t=116, l=108, i=105, n=110}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/associate-to.html)

    