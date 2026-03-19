

# bufferedReader

Returns a new BufferedReader for reading the content of this file.

```kotlin
inline fun File.bufferedReader(charset: Charset = Charsets.UTF_8, bufferSize: Int = DEFAULT_BUFFER_SIZE): BufferedReader(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("example.txt")

    // Read the file line by line using BufferedReader
    file.bufferedReader().use { reader ->
        reader.lineSequence().forEach { line ->
            println(line)
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/buffered-reader.html)

    