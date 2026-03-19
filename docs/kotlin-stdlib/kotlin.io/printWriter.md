

# printWriter

Returns a new PrintWriter for writing the content of this file.

```kotlin
inline fun File.printWriter(charset: Charset = Charsets.UTF_8): PrintWriter(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("example.txt")
    file.printWriter().use { writer ->
        writer.println("Hello, Kotlin!")
        writer.println("This file was written with printWriter.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/print-writer.html)

    