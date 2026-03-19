

# writeLines

Write the specified collection of char sequences lines to a file terminating each one with the platform's line separator.

```kotlin
@IgnorableReturnValueinline fun Path.writeLines(lines: Iterable<CharSequence>, charset: Charset = Charsets.UTF_8, vararg options: OpenOption): Path(source)
```

```kotlin
import java.nio.file.*
import kotlin.io.path.*

fun main() {
    val path = Path.of("example.txt")
    val lines = listOf(
        "Hello, world!",
        "This is the second line.",
        "Goodbye!"
    )
    path.writeLines(lines)   // creates the file if it doesn't exist
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/write-lines.html)

    