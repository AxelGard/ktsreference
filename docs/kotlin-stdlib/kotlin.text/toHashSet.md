

# toHashSet

Returns a new HashSet of all characters.

```kotlin
fun CharSequence.toHashSet(): HashSet<Char>(source)
```

```kotlin
fun main() {
    val text = "hello world"
    val uniqueChars: HashSet<Char> = text.toHashSet()

    println(uniqueChars)   // prints: [h, e, l, o,  , w, r, d]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-hash-set.html)

    