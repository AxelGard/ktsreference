

# createFile

Creates a new and empty file specified by this path, failing if the file already exists.

```kotlin
@IgnorableReturnValueinline fun Path.createFile(vararg attributes: FileAttribute<*>): Path(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.createFile

fun main() {
    val filePath = Paths.get("example.txt")
    filePath.createFile()
    println("Created file at ${filePath.toAbsolutePath()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/create-file.html)

    