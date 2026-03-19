

# isReadable

Checks if the file located by this path exists and is readable.

```kotlin
inline fun Path.isReadable(): Boolean(source)
```

```kotlin
import java.nio.file.Path
import java.nio.file.Paths

fun main() {
    val path: Path = Paths.get("example.txt")

    if (path.isReadable()) {
        println("The file exists and is readable.")
    } else {
        println("The file does not exist or is not readable.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/is-readable.html)

    