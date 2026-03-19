

# isTitleCase

Returns true if this character is a title case letter.

```kotlin
expect fun Char.isTitleCase(): Boolean(source)
```

```kotlin
fun main() {
    val text = "Hello World! This Is Kotlin."
    val titleCaseCount = text.count { it.isTitleCase() }
    println("Number of title‑case letters: $titleCaseCount")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-title-case.html)

    