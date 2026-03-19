

# deleteExisting

Deletes the existing file or empty directory specified by this path.

```kotlin
inline fun Path.deleteExisting()(source)
```

```kotlin
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths
import kotlin.io.path.deleteExisting

fun main() {
    val path: Path = Paths.get("example.txt")

    // Create the file and write some content
    Files.writeString(path, "Hello, world!")

    // Delete the file if it exists
    path.deleteExisting()

    // Verify deletion
    println("File exists after deleteExisting: ${Files.exists(path)}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/delete-existing.html)

    