

# readLines

Reads the file content as a list of lines.

```kotlin
fun File.readLines(charset: Charset = Charsets.UTF_8): List<String>(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("example.txt")
    val lines: List<String> = file.readLines()   // reads the file using UTF‑8 by default
    lines.forEach { println(it) }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/read-lines.html)

    