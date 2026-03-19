

# writeText

Sets the content of this file as text encoded using UTF-8 or the specified charset.

```kotlin
fun Path.writeText(text: CharSequence, charset: Charset = Charsets.UTF_8, vararg options: OpenOption)(source)
```

```kotlin
import java.nio.file.Path
import java.nio.file.Paths
import kotlin.io.path.writeText

fun main() {
    val path: Path = Paths.get("example.txt")
    path.writeText("Hello, Kotlin!")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/write-text.html)

    