

# createDirectories

Creates a directory ensuring that all nonexistent parent directories exist by creating them first.

```kotlin
@IgnorableReturnValueinline fun Path.createDirectories(vararg attributes: FileAttribute<*>): Path(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.*

fun main() {
    val dir = Paths.get("output", "reports")
    dir.createDirectories()   // creates /output/reports, plus any missing parents
    println("Directory created at: ${dir.toAbsolutePath()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/create-directories.html)

    