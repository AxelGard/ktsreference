

# mapIndexedTo

Applies the given transform function to each character and its index in the original char sequence and appends the results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <R, C : MutableCollection<in R>> CharSequence.mapIndexedTo(destination: C, transform: (index: Int, Char) -> R): C(source)
```

```kotlin
val text = "hello"
val result = mutableListOf<String>()
text.mapIndexedTo(result) { index, ch -> "[$index] $ch" }
println(result)   // Prints: [ [0] h, [1] e, [2] l, [3] l, [4] o ]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/map-indexed-to.html)

    