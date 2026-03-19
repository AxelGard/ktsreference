

# isRegularFile

Checks if the file located by this path is a regular file.

```kotlin
inline fun Path.isRegularFile(vararg options: LinkOption): Boolean(source)
```

```kotlin
import java.nio.file.Paths

fun main() {
    val path = Paths.get("example.txt")

    if (path.isRegularFile()) {
        println("${path.fileName} is a regular file.")
    } else {
        println("${path.fileName} is not a regular file.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/is-regular-file.html)

    