

# bufferedReader

Returns a new BufferedReader for reading the content of this file.

```kotlin
inline fun Path.bufferedReader(charset: Charset = Charsets.UTF_8, bufferSize: Int = DEFAULT_BUFFER_SIZE, vararg options: OpenOption): BufferedReader(source)
```

```kotlin
import java.nio.file.Paths
import java.nio.charset.Charset

fun main() {
    val path = Paths.get("example.txt")
    path.bufferedReader(Charsets.UTF_8).use { reader ->
        reader.lineSequence().forEach { line ->
            println(line)
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/buffered-reader.html)

    