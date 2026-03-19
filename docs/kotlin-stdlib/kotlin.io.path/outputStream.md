

# outputStream

Constructs a new OutputStream of this file and returns it as a result.

```kotlin
inline fun Path.outputStream(vararg options: OpenOption): OutputStream(source)
```

```kotlin
import java.nio.file.*
import java.nio.file.StandardOpenOption.*

fun main() {
    val path = Paths.get("example.txt")
    path.outputStream(CREATE, WRITE, TRUNCATE_EXISTING).use { out ->
        out.write("Hello, Kotlin!".toByteArray())
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/output-stream.html)

    