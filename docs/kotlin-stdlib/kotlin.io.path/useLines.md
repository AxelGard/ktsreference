

# useLines

Calls the block callback giving it a sequence of all the lines in this file and closes the reader once the processing is complete.

```kotlin
@IgnorableReturnValueinline fun <T> Path.useLines(charset: Charset = Charsets.UTF_8, block: (Sequence<String>) -> T): T(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.useLines

fun main() {
    val path = Paths.get("example.txt")

    // Count the number of non‑blank lines in the file
    val lineCount = path.useLines { lines ->
        lines.count { it.isNotBlank() }
    }

    println("Number of non‑blank lines: $lineCount")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/use-lines.html)

    