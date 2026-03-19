

# prependIndent

Prepends indent to every line of the original string.

```kotlin
fun String.prependIndent(indent: String = "    "): String(source)
```

```kotlin
fun main() {
    val original = """
        First line
        Second line
    """.trimIndent()

    val indented = original.prependIndent(">> ")

    println(indented)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/prepend-indent.html)

    