

# deleteRecursively

Delete this file with all its children. Note that if this operation fails then partial deletion may have taken place.

```kotlin
@IgnorableReturnValuefun File.deleteRecursively(): Boolean(source)
```

```kotlin
import java.io.File

fun main() {
    // Create a temporary directory with some nested files
    val rootDir = File("exampleDir")
    rootDir.mkdirs()
    File(rootDir, "file1.txt").writeText("Hello")
    val subDir = File(rootDir, "sub")
    subDir.mkdirs()
    File(subDir, "file2.txt").writeText("World")

    // Delete the directory and all its contents recursively
    val deleted = rootDir.deleteRecursively()
    println("Deletion successful: $deleted")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/delete-recursively.html)

    