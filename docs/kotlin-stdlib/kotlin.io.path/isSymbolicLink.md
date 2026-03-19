

# isSymbolicLink

Checks if the file located by this path exists and is a symbolic link.

```kotlin
inline fun Path.isSymbolicLink(): Boolean(source)
```

```kotlin
import java.nio.file.Path
import kotlin.io.path.isSymbolicLink

fun main() {
    val path: Path = Path.of("example.txt")

    if (path.isSymbolicLink()) {
        println("$path is a symbolic link.")
    } else {
        println("$path is not a symbolic link.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/is-symbolic-link.html)

    