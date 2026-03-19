

# flatMapTo

Appends all elements yielded from results of transform function being invoked on each character of original char sequence, to the given destination.

```kotlin
@IgnorableReturnValueinline fun <R, C : MutableCollection<in R>> CharSequence.flatMapTo(destination: C, transform: (Char) -> Iterable<R>): C(source)
```

```kotlin
fun main() {
    val input: CharSequence = "abc"
    val destination = mutableListOf<String>()

    input.flatMapTo(destination) { ch ->
        // For each character, emit the character itself and its uppercase variant
        listOf(ch.toString(), ch.uppercaseChar().toString())
    }

    println(destination)   // prints: [a, A, b, B, c, C]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/flat-map-to.html)

    