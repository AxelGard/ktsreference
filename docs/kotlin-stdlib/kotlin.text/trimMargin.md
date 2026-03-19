

# trimMargin

Trims leading whitespace characters followed by marginPrefix from every line of a source string and removes the first and the last lines if they are blank (notice difference blank vs empty).

```kotlin
fun String.trimMargin(marginPrefix: String = "|"): String(source)
```

```kotlin
val text = """
    |Hello, world!
    |  This line is indented.
    |Goodbye, world!
""".trimMargin()

println(text)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim-margin.html)

    