

# fileStore

Returns the FileStore representing the file store where a file is located.

```kotlin
inline fun Path.fileStore(): FileStore(source)
```

```kotlin
import java.nio.file.Files
import java.nio.file.Paths
import kotlin.io.path.fileStore

fun main() {
    // Path to a file on the file system
    val path = Paths.get("/tmp/example.txt")

    // Ensure the file exists for the demo
    if (!Files.exists(path)) {
        Files.createFile(path)
    }

    // Obtain the FileStore that hosts the file
    val fileStore = path.fileStore()

    // Print some useful information about the file store
    println("File: ${path}")
    println("File store name: ${fileStore.name}")
    println("File store type: ${fileStore.type}")
    println("Total space: ${fileStore.totalSpace} bytes")
    println("Unallocated space: ${fileStore.unallocatedSpace} bytes")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/file-store.html)

    