

# appendLines

Appends the specified collection of char sequences lines to a file terminating each one with the platform's line separator.

```kotlin
@IgnorableReturnValueinline fun Path.appendLines(lines: Iterable<CharSequence>, charset: Charset = Charsets.UTF_8): Path(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.appendLines
import kotlin.io.path.createFile
import kotlin.io.path.exists

fun main() {
    val file: Path = Paths.get("output.txt")

    // Ensure the file exists before appending
    if (!file.exists()) file.createFile()

    val lines = listOf(
        "First line",
        "Second line",
        "Third line"
    )

    // Append the lines to the file
    file.appendLines(lines)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/append-lines.html)

    