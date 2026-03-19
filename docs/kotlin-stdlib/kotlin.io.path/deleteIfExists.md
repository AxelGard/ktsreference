

# deleteIfExists

Deletes the file or empty directory specified by this path if it exists.

```kotlin
@IgnorableReturnValueinline fun Path.deleteIfExists(): Boolean(source)
```

```kotlin
import kotlin.io.path.*
import java.nio.file.Files

fun main() {
    // Create a temporary file
    val tempFile = Files.createTempFile("sample", ".txt")

    // Write some content to the file
    tempFile.writeText("This is a test file.")

    // Delete the file if it exists
    val wasDeleted = tempFile.deleteIfExists()

    // Output the result
    println("File deleted: $wasDeleted")   // Should print: File deleted: true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/delete-if-exists.html)

    