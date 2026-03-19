

# fileSize

Returns the size of a regular file as a Long value of bytes or throws an exception if the file doesn't exist.

```kotlin
inline fun Path.fileSize(): Long(source)
```

```kotlin
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths

fun main() {
    val path: Path = Paths.get("example.txt")

    // Ensure the file exists for the example
    if (!Files.exists(path)) {
        Files.writeString(path, "Hello, world!")
    }

    val sizeInBytes: Long = path.fileSize()
    println("Size of '${path.fileName}': $sizeInBytes bytes")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/file-size.html)

    