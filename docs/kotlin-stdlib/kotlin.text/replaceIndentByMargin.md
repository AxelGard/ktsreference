

# replaceIndentByMargin

Detects indent by marginPrefix as it does trimMargin and replace it with newIndent.

```kotlin
fun String.replaceIndentByMargin(newIndent: String = "", marginPrefix: String = "|"): String(source)
```

```kotlin
val source = """
    |    first line
    |    second line
""".trimIndent()

// Replace the indent before the margin prefix with a tab character
val result = source.replaceIndentByMargin(newIndent = "\t", marginPrefix = "|")

println(result)
// Output:
//     first line
//     second line
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/replace-indent-by-margin.html)

    