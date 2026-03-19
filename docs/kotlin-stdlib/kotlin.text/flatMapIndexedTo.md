

# flatMapIndexedTo

Appends all elements yielded from results of transform function being invoked on each character and its index in the original char sequence, to the given destination.

```kotlin
@JvmName(name = "flatMapIndexedIterableTo")@IgnorableReturnValueinline fun <R, C : MutableCollection<in R>> CharSequence.flatMapIndexedTo(destination: C, transform: (index: Int, Char) -> Iterable<R>): C(source)
```

```kotlin
val result = mutableListOf<String>()

"abc".flatMapIndexedTo(result) { index, char ->
    // For each character, produce a list containing two strings:
    // 1. The character itself
    // 2. The character's ASCII code as a string
    listOf(char.toString(), char.code.toString())
}

println(result)  // Output: [a, 97, b, 98, c, 99]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/flat-map-indexed-to.html)

    