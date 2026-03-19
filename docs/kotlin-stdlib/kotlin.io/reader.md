

# reader

Returns a new FileReader for reading the content of this file.

```kotlin
inline fun File.reader(charset: Charset = Charsets.UTF_8): InputStreamReader(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("example.txt")

    // Use the reader to read the file line by line
    file.reader().use { reader ->
        reader.lineSequence().forEach { line ->
            println(line)
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/reader.html)

    