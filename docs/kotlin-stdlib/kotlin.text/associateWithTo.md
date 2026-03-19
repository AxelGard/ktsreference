

# associateWithTo

Populates and returns the destination mutable map with key-value pairs for each character of the given char sequence, where key is the character itself and value is provided by the valueSelector function applied to that key.

```kotlin
@IgnorableReturnValueinline fun <V, M : MutableMap<in Char, in V>> CharSequence.associateWithTo(destination: M, valueSelector: (Char) -> V): M(source)
```

```kotlin
val text = "Kotlin"
val map = mutableMapOf<Char, String>()

text.associateWithTo(map) { c -> c.lowercaseChar().toString() }

println(map)   // prints: {K=k, o=o, t=t, l=l, i=i, n=n}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/associate-with-to.html)

    