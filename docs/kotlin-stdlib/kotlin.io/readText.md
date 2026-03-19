

# readText

Gets the entire content of this file as a String using UTF-8 or specified charset.

```kotlin
fun File.readText(charset: Charset = Charsets.UTF_8): String(source)
```

```kotlin
import java.io.File
import java.nio.charset.Charset

fun main() {
    val file = File("example.txt")
    val content = file.readText()                 // uses UTF‑8 by default
    // val content = file.readText(Charsets.ISO_8859_1) // optional charset

    println(content)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/read-text.html)

    