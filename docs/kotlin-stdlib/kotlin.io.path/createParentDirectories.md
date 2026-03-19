

# createParentDirectories

Ensures that all parent directories of this path exist, creating them if required.

```kotlin
@IgnorableReturnValuefun Path.createParentDirectories(vararg attributes: FileAttribute<*>): Path(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.createParentDirectories
import kotlin.io.path.writeText

fun main() {
    // Define a file path that includes non‑existent parent directories
    val file = Paths.get("tmp/dir1/dir2/file.txt")

    // Create all missing parent directories
    file.parent.createParentDirectories()

    // Write some content to the file
    file.writeText("Hello, world!")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/create-parent-directories.html)

    