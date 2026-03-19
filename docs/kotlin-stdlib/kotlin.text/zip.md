

# zip

Returns a list of pairs built from the characters of this and the other char sequences with the same index The returned list has length of the shortest char sequence.

```kotlin
infix fun CharSequence.zip(other: CharSequence): List<Pair<Char, Char>>(source)
```

```kotlin
fun main() {
    val first = "hello"
    val second = "world"
    val zipped = first zip second
    println(zipped) // [(h, w), (e, o), (l, r), (l, l), (o, d)]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/zip.html)

    