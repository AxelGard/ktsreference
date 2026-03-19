

# replaceIndent

Detects a common minimal indent like it does trimIndent and replaces it with the specified newIndent.

```kotlin
fun String.replaceIndent(newIndent: String = ""): String(source)
```

```kotlin
val text = """
    |    first line
    |    second line
    |    third line
""".trimMargin()

val result = text.replaceIndent("  ")  // replace minimal indent with two spaces

println(result)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace-indent.html)

    