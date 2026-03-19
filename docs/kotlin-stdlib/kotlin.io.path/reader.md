

# reader

Returns a new InputStreamReader for reading the content of this file.

```kotlin
inline fun Path.reader(charset: Charset = Charsets.UTF_8, vararg options: OpenOption): InputStreamReader(source)
```

```kotlin
import java.nio.file.*
import java.nio.charset.Charset
import kotlin.io.path.*

fun main() {
    // Create a temporary file and write some text to it
    val tempFile = Files.createTempFile("example", ".txt")
    tempFile.toFile().writeText("Hello\nWorld", Charsets.UTF_8)

    // Read the file using Path.reader()
    tempFile.reader(Charsets.UTF_8).use { reader ->
        reader.forEachLine { line ->
            println(line)
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/reader.html)

    