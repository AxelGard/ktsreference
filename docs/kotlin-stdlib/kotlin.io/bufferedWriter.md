

# bufferedWriter

Returns a new BufferedWriter for writing the content of this file.

```kotlin
inline fun File.bufferedWriter(charset: Charset = Charsets.UTF_8, bufferSize: Int = DEFAULT_BUFFER_SIZE): BufferedWriter(source)
```

```kotlin
import java.io.File
import java.nio.charset.Charset

fun main() {
    val file = File("sample.txt")
    // Write text to the file using a BufferedWriter with default charset and buffer size
    file.bufferedWriter(Charsets.UTF_8, 8192).use { writer ->
        writer.write("Line 1: Hello, World!\n")
        writer.write("Line 2: Kotlin I/O is simple.\n")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/buffered-writer.html)

    