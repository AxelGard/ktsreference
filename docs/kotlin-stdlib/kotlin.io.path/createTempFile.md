

# createTempFile

Creates an empty file in the default temp directory, using the given prefix and suffix to generate its name.

```kotlin
inline fun createTempFile(prefix: String? = null, suffix: String? = null, vararg attributes: FileAttribute<*>): Path(source)
```

```kotlin
import java.nio.file.Files
import java.nio.file.Paths
import java.nio.file.attribute.FileAttribute

fun main() {
    // Create a temporary file with a custom prefix and suffix
    val tempFile = Files.createTempFile(
        prefix = "demo-",
        suffix = ".txt",
        FileAttribute<Any>() // no special attributes
    )

    // Write some content to the file
    Files.writeString(tempFile, "Hello, temporary file!")

    // Read and print the content
    val content = Files.readString(tempFile)
    println(content)

    // Clean up: delete the temporary file
    Files.deleteIfExists(tempFile)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/create-temp-file.html)

    