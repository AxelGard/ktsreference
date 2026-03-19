

# isDirectory

Checks if the file located by this path is a directory.

```kotlin
inline fun Path.isDirectory(vararg options: LinkOption): Boolean(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.isDirectory

fun main() {
    val path = Paths.get("src")

    if (path.isDirectory()) {
        println("$path is a directory")
    } else {
        println("$path is not a directory")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/is-directory.html)

    