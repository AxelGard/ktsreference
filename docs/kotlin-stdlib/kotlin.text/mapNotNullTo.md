

# mapNotNullTo

Applies the given transform function to each character in the original char sequence and appends only the non-null results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <R : Any, C : MutableCollection<in R>> CharSequence.mapNotNullTo(destination: C, transform: (Char) -> R?): C(source)
```

```kotlin
val text = "a1b2c3"
val digits = mutableListOf<Int>()

text.mapNotNullTo(digits) { ch ->
    if (ch.isDigit()) ch.toString().toInt() else null
}

// digits now contains [1, 2, 3]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/map-not-null-to.html)

    