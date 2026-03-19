

# createTempFile

Warning since 1.4

```kotlin
fun createTempFile(prefix: String = "tmp", suffix: String? = null, directory: File? = null): File(source)
```

```kotlin
import java.io.File

fun main() {
    // Create a temporary file with a custom prefix and suffix
    val tempFile: File = File.createTempFile(prefix = "myTemp_", suffix = ".txt")

    println("Temporary file created at: ${tempFile.absolutePath}")

    // Write some content to the temporary file
    tempFile.writeText("Hello, temporary file!")

    // Read the content back
    val content = tempFile.readText()
    println("File content: $content")

    // Schedule the file for deletion when the JVM exits
    tempFile.deleteOnExit()
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/create-temp-file.html)

    