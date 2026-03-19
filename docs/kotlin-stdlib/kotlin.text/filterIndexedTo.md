

# filterIndexedTo

Appends all characters matching the given predicate to the given destination.

```kotlin
@IgnorableReturnValueinline fun <C : Appendable> CharSequence.filterIndexedTo(destination: C, predicate: (index: Int, Char) -> Boolean): C(source)
```

```kotlin
fun main() {
    val source = "Kotlin 1.8.20"
    val destination = StringBuilder()

    // Append only the characters that are at odd indices
    source.filterIndexedTo(destination) { index, ch ->
        index % 2 == 1
    }

    println(destination.toString())   // prints the filtered characters
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/filter-indexed-to.html)

    