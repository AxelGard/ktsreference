

# writer

Returns a new FileWriter for writing the content of this file.

```kotlin
inline fun File.writer(charset: Charset = Charsets.UTF_8): OutputStreamWriter(source)
```

```kotlin
import java.io.File
import java.nio.charset.Charset

fun main() {
    val file = File("example.txt")

    // Write text using the default UTF‑8 charset
    file.writer().use { out ->
        out.write("Hello, Kotlin writer!\n")
        out.write("This is a simple example.\n")
    }

    // Write text using a different charset (optional)
    file.writer(Charset.forName("ISO-8859-1")).use { out ->
        out.write("Another line with a different charset.\n")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/writer.html)

    