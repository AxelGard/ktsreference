

# filter

Returns a char sequence containing only those characters from the original char sequence that match the given predicate.

```kotlin
inline fun CharSequence.filter(predicate: (Char) -> Boolean): CharSequence(source)
```

fun main() {
    val input = "Kotlin 1.8.10"
    val digits = input.filter { it.isDigit() }
    println(digits)
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/filter.html)

    