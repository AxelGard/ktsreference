

# outputStream

Constructs a new FileOutputStream of this file and returns it as a result.

```kotlin
inline fun File.outputStream(): FileOutputStream(source)
```

```kotlin
import java.io.File
import java.nio.charset.Charset

fun main() {
    val file = File("example.txt")

    // Obtain a FileOutputStream for the file and write data to it
    file.outputStream().use { out ->
        out.write("Hello, world!".toByteArray(Charset.forName("UTF-8")))
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/output-stream.html)

    