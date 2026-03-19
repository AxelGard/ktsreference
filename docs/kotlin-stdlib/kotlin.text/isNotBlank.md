

# isNotBlank

Returns true if this char sequence is not empty and contains some characters except whitespace characters.

```kotlin
inline fun CharSequence.isNotBlank(): Boolean(source)
```

```kotlin
fun main() {
    val text = "  Hello, world!  "
    if (text.isNotBlank()) {
        println("The text is not blank.")
    } else {
        println("The text is blank or only whitespace.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-not-blank.html)

    