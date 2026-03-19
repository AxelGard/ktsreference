

# mapTo

Applies the given transform function to each character of the original char sequence and appends the results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <R, C : MutableCollection<in R>> CharSequence.mapTo(destination: C, transform: (Char) -> R): C(source)
```

fun main() {
    val source: CharSequence = "Hello"
    val asciiCodes = mutableListOf<Int>()
    source.mapTo(asciiCodes) { it.code }
    println(asciiCodes) // [72, 101, 108, 108, 111]
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/map-to.html)

    