

# buffered

Creates a BufferedInputStream wrapping this stream.

```kotlin
inline fun InputStream.buffered(bufferSize: Int = DEFAULT_BUFFER_SIZE): BufferedInputStream(source)
```

```kotlin
import java.io.File
import java.io.InputStream
import java.io.BufferedInputStream

fun main() {
    // Open a file input stream
    val input: InputStream = File("sample.txt").inputStream()

    // Wrap it with a BufferedInputStream using the Kotlin extension
    input.buffered().use { bufferedInput ->
        // Read the entire file as a string
        val content = bufferedInput.readBytes().toString(Charsets.UTF_8)
        println(content)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/buffered.html)

    