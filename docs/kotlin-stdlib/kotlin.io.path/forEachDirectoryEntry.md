

# forEachDirectoryEntry

Performs the given action on each entry in this directory optionally filtered by matching against the specified glob pattern.

```kotlin
inline fun Path.forEachDirectoryEntry(glob: String = "*", action: (Path) -> Unit)(source)
```

```kotlin
import kotlin.io.path.*
import java.nio.file.Path

fun main() {
    val dir: Path = Path.of("src")          // the directory to scan
    dir.forEachDirectoryEntry("*.kt") { entry ->
        println("Found Kotlin file: ${entry.fileName}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/for-each-directory-entry.html)

    