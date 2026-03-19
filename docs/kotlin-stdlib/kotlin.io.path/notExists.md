

# notExists

Checks if the file located by this path does not exist.

```kotlin
inline fun Path.notExists(vararg options: LinkOption): Boolean(source)
```

```kotlin
import java.nio.file.Path
import java.nio.file.LinkOption

fun main() {
    val path: Path = Path.of("example.txt")

    if (path.notExists()) {
        println("File ${path} does not exist.")
    } else {
        println("File ${path} exists.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/not-exists.html)

    