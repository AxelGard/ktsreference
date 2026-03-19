

# setLastModifiedTime

Sets the last modified time attribute for the file located by this path.

```kotlin
inline fun Path.setLastModifiedTime(value: FileTime): Path(source)
```

```kotlin
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths
import java.nio.file.attribute.FileTime
import java.time.Instant

fun main() {
    val path: Path = Paths.get("example.txt")

    // Create the file if it doesn't exist
    if (!Files.exists(path)) {
        Files.createFile(path)
    }

    // Set the last modified time to the current instant
    val fileTime: FileTime = FileTime.from(Instant.now())
    path.setLastModifiedTime(fileTime)

    println("Last modified time of ${path.fileName} set to $fileTime")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/set-last-modified-time.html)

    