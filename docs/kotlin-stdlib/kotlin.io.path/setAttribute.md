

# setAttribute

Sets the value of a file attribute.

```kotlin
@IgnorableReturnValueinline fun Path.setAttribute(attribute: String, value: Any?, vararg options: LinkOption): Path(source)
```

```kotlin
import java.nio.file.Files
import java.nio.file.attribute.FileTime

fun main() {
    // Create a temporary file
    val path = Files.createTempFile("demo", ".txt")

    // Set the file's last modified time to one hour ago
    path.setAttribute(
        "basic:lastModifiedTime",
        FileTime.fromMillis(System.currentTimeMillis() - 3_600_000)
    )

    // Verify the change
    val time = Files.getAttribute(path, "basic:lastModifiedTime") as FileTime
    println("Updated lastModifiedTime: $time")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/set-attribute.html)

    