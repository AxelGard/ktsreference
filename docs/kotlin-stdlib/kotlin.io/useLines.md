

# useLines

Calls the block callback giving it a sequence of all the lines in this file and closes the reader once the processing is complete.

```kotlin
inline fun <T> File.useLines(charset: Charset = Charsets.UTF_8, block: (Sequence<String>) -> T): T(source)
```

```kotlin
import java.io.File
import java.nio.charset.Charset

fun main() {
    val file = File("data.txt")

    // Count the number of lines in the file
    val lineCount = file.useLines { lines ->
        lines.count()
    }

    println("Total lines: $lineCount")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/use-lines.html)

    