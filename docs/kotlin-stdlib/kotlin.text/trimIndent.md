

# trimIndent

Detects a common minimal indent of all the input lines, removes it from every line and also removes the first and the last lines if they are blank (notice difference blank vs empty).

```kotlin
fun String.trimIndent(): String(source)
```

```kotlin
fun main() {
    val text = """
    
        |    Hello, Kotlin!
        |    Trim indentation.
    
    """.trimIndent()
    println(text)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/trim-indent.html)

    