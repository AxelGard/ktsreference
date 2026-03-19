

# useDirectoryEntries

Calls the block callback with a sequence of all entries in this directory optionally filtered by matching against the specified glob pattern.

```kotlin
@IgnorableReturnValueinline fun <T> Path.useDirectoryEntries(glob: String = "*", block: (Sequence<Path>) -> T): T(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.useDirectoryEntries

fun main() {
    val dir: Path = Paths.get("myFolder")

    dir.useDirectoryEntries("*.txt") { entries ->
        entries.forEach { file ->
            println("Found file: $file")
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/use-directory-entries.html)

    