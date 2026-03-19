

# createDirectory

Creates a new directory or throws an exception if there is already a file or directory located by this path.

```kotlin
@IgnorableReturnValueinline fun Path.createDirectory(vararg attributes: FileAttribute<*>): Path(source)
```

```kotlin
import java.nio.file.attribute.PosixFilePermission
import java.nio.file.attribute.PosixFilePermissions
import kotlin.io.path.*

fun main() {
    // Path where the new directory will be created
    val dirPath = "demoDir".toPath()

    // Optional file permissions attribute (e.g., rwx for owner, r-x for group, --- for others)
    val perms = PosixFilePermissions.fromString("rwxr-x---")
    val attrs = PosixFilePermissions.asFileAttribute(perms)

    // Create the directory
    dirPath.createDirectory(attrs)

    println("Directory created at: ${dirPath.toAbsolutePath()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/create-directory.html)

    