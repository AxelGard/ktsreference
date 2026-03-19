

# forEachLine

Reads this file line by line using the specified charset and calls action for each line. Default charset is UTF-8.

```kotlin
inline fun Path.forEachLine(charset: Charset = Charsets.UTF_8, action: (line: String) -> Unit)(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.*

fun main() {
    val filePath = Paths.get("sample.txt")
    filePath.forEachLine { line ->
        println(line)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/for-each-line.html)

    