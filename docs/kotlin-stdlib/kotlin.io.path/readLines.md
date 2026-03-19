

# readLines

Reads the file content as a list of lines.

```kotlin
inline fun Path.readLines(charset: Charset = Charsets.UTF_8): List<String>(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.readLines

fun main() {
    val path = Paths.get("example.txt")
    val lines = path.readLines()          // reads the file as a list of strings
    lines.forEachIndexed { i, line ->
        println("Line ${i + 1}: $line")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/read-lines.html)

    