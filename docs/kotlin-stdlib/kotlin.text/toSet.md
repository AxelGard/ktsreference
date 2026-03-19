

# toSet

Returns a Set of all characters.

```kotlin
fun CharSequence.toSet(): Set<Char>(source)
```

```kotlin
fun main() {
    val text = "kotlin"
    val uniqueChars: Set<Char> = text.toSet()
    println(uniqueChars)   // Output: [k, o, l, t, i, n]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-set.html)

    