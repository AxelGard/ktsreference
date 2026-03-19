

# matches

Returns true if this char sequence matches the given regular expression.

```kotlin
infix inline fun CharSequence.matches(regex: Regex): Boolean(source)
```

```kotlin
fun main() {
    val text = "Kotlin123"
    val numberRegex = Regex("\\d+")

    // Infix usage of CharSequence.matches
    if (text matches numberRegex) {
        println("The text consists only of digits.")
    } else {
        println("The text contains non‑digit characters.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/matches.html)

    