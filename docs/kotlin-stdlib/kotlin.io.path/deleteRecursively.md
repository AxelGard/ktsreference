

# deleteRecursively

Recursively deletes this directory and its content. Note that if this function throws, partial deletion may have taken place.

```kotlin
@ExperimentalPathApifun Path.deleteRecursively()(source)
```

```kotlin
import java.nio.file.Files
import kotlin.io.path.ExperimentalPathApi
import kotlin.io.path.deleteRecursively
import kotlin.io.path.exists
import kotlin.io.path.resolve
import kotlin.io.path.writeText

@OptIn(ExperimentalPathApi::class)
fun main() {
    // Create a temporary directory with nested files
    val rootDir = Files.createTempDirectory("demo").toPath()
    val file = rootDir.resolve("file.txt")
    val subDir = rootDir.resolve("sub")
    Files.createDirectory(subDir)
    val subFile = subDir.resolve("subfile.txt")

    file.writeText("Hello")
    subFile.writeText("World")

    println("Before deletion: ${rootDir.exists()}")
    // Recursively delete the directory and all its contents
    rootDir.deleteRecursively()
    println("After deletion: ${rootDir.exists()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/delete-recursively.html)

    