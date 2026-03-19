

# bufferedWriter

Returns a new BufferedWriter for writing the content of this file.

```kotlin
inline fun Path.bufferedWriter(charset: Charset = Charsets.UTF_8, bufferSize: Int = DEFAULT_BUFFER_SIZE, vararg options: OpenOption): BufferedWriter(source)
```

```kotlin
import java.nio.file.Paths
import java.nio.file.StandardOpenOption
import kotlin.io.path.bufferedWriter

fun main() {
    val path = Paths.get("output.txt")
    path.bufferedWriter(StandardOpenOption.CREATE, StandardOpenOption.APPEND).use { writer ->
        writer.write("Hello, world!\n")
        writer.write("This is a second line.\n")
    }
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/buffered-writer.html)

    