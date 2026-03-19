

# toCollection

Appends all characters to the given destination collection.

```kotlin
@IgnorableReturnValuefun <C : MutableCollection<in Char>> CharSequence.toCollection(destination: C): C(source)
```

```kotlin
val text = "Hello, Kotlin!"
val chars = mutableListOf<Char>()

text.toCollection(chars)   // appends every character of 'text' to 'chars'

println(chars) // prints: [H, e, l, l, o, ,,  , K, o, t, l, i, n, !]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-collection.html)

    