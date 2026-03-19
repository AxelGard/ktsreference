

# replaceFirstChar

Returns a copy of this string having its first character replaced with the result of the specified transform, or the original string if it's empty.

```kotlin
@JvmName(name = "replaceFirstCharWithChar")inline fun String.replaceFirstChar(transform: (Char) -> Char): String(source)
```

```kotlin
fun main() {
    val text = "kotlin"
    val transformed = text.replaceFirstChar { it.uppercaseChar() }
    println(transformed) // Output: Kotlin
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace-first-char.html)

    