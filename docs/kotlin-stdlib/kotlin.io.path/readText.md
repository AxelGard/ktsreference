

# readText

Gets the entire content of this file as a String using UTF-8 or the specified charset.

```kotlin
fun Path.readText(charset: Charset = Charsets.UTF_8): String(source)
```

import java.nio.file.Paths
import kotlin.io.path.readText

fun main() {
    val filePath = Paths.get("sample.txt")
    val content = filePath.readText()
    println(content)
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/read-text.html)

    