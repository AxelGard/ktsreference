

# writer

Returns a new OutputStreamWriter for writing the content of this file.

```kotlin
inline fun Path.writer(charset: Charset = Charsets.UTF_8, vararg options: OpenOption): OutputStreamWriter(source)
```

```kotlin
import java.nio.file.*
import java.nio.charset.*

fun main() {
    val path = Paths.get("example.txt")
    path.writer(Charsets.UTF_8, StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING)
        .use { writer ->
            writer.write("Hello, Kotlin writer!")
        }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/writer.html)

    