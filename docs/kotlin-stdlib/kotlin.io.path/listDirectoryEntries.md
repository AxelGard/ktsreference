

# listDirectoryEntries

Returns a list of the entries in this directory optionally filtered by matching against the specified glob pattern.

```kotlin
fun Path.listDirectoryEntries(glob: String = "*"): List<Path>(source)
```

```kotlin
import kotlin.io.path.*
import java.nio.file.Paths

fun main() {
    val dir = Paths.get("src")

    // List all entries in the directory
    val allEntries = dir.listDirectoryEntries()
    println("All entries:")
    allEntries.forEach { println(it.fileName) }

    // List only Kotlin source files
    val kotlinFiles = dir.listDirectoryEntries("*.kt")
    println("\nKotlin files:")
    kotlinFiles.forEach { println(it.fileName) }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/list-directory-entries.html)

    