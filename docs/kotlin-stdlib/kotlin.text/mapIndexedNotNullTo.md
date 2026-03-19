

# mapIndexedNotNullTo

Applies the given transform function to each character and its index in the original char sequence and appends only the non-null results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <R : Any, C : MutableCollection<in R>> CharSequence.mapIndexedNotNullTo(destination: C, transform: (index: Int, Char) -> R?): C(source)
```

```kotlin
val input = "a1b2c3"
val digitIndices = mutableListOf<Int>()

input.mapIndexedNotNullTo(digitIndices) { index, ch ->
    if (ch.isDigit()) index else null
}

println(digitIndices) // prints: [1, 3, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/map-indexed-not-null-to.html)

    