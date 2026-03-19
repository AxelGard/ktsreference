

# lineSequence

Splits this char sequence to a sequence of lines delimited by any of the following character sequences: CRLF, LF or CR.

```kotlin
fun CharSequence.lineSequence(): Sequence<String>(source)
```

```kotlin
val text = """
    First line
    Second line
    Third line
""".trimIndent()

text.lineSequence().forEachIndexed { index, line ->
    println("${index + 1}: $line")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/line-sequence.html)

    