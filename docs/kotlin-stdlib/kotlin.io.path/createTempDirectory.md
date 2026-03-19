

# createTempDirectory

Creates a new directory in the default temp directory, using the given prefix to generate its name.

```kotlin
inline fun createTempDirectory(prefix: String? = null, vararg attributes: FileAttribute<*>): Path(source)
```

```kotlin
import kotlin.io.path.*
import java.nio.file.Files
import java.nio.file.Path

fun main() {
    // Create a temporary directory with a custom prefix
    val tempDir: Path = createTempDirectory("myApp-")

    println("Temporary directory created at: $tempDir")

    // Create a file inside the temporary directory
    val tempFile = tempDir.resolve("sample.txt")
    tempFile.writeText("Hello, temporary world!")

    println("Written to file: $tempFile")
    println("File contents: ${tempFile.readText()}")

    // Clean up: delete the file and the directory
    Files.walk(tempDir).sorted(Comparator.reverseOrder()).forEach { Files.delete(it) }

    println("Temporary directory and its contents have been deleted.")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/create-temp-directory.html)

    