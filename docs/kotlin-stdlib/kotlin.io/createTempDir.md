

# createTempDir

Warning since 1.4

```kotlin
fun createTempDir(prefix: String = "tmp", suffix: String? = null, directory: File? = null): File(source)
```

```kotlin
import java.io.File

fun main() {
    // Create a temporary directory with default prefix "tmp"
    val tempDir: File = createTempDir()
    println("Temporary directory created at: ${tempDir.absolutePath}")

    // Example: create a temporary file inside the temp directory
    val tempFile = File(tempDir, "example.txt")
    tempFile.writeText("Hello, world!")
    println("Temporary file created at: ${tempFile.absolutePath}")

    // Clean up: delete the temporary file and directory
    tempFile.delete()
    tempDir.delete()
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/create-temp-dir.html)

    