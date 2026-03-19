

# appendText

Appends text to the content of this file using UTF-8 or the specified charset.

```kotlin
fun Path.appendText(text: CharSequence, charset: Charset = Charsets.UTF_8)(source)
```

```kotlin
import java.nio.file.Path
import java.nio.file.Paths

fun main() {
    val path: Path = Paths.get("example.txt")
    path.appendText("Hello, world!\n")
    path.appendText("This is appended to the file.\n")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/append-text.html)

    