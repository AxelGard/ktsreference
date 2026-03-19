

# setPosixFilePermissions

Sets the POSIX file permissions for the file located by this path.

```kotlin
inline fun Path.setPosixFilePermissions(value: Set<PosixFilePermission>): Path(source)
```

```kotlin
import java.nio.file.Files
import java.nio.file.Paths
import java.nio.file.attribute.PosixFilePermission
import kotlin.io.path.setPosixFilePermissions

fun main() {
    val path = Paths.get("example.txt")

    // Create the file if it doesn't exist
    if (!Files.exists(path)) Files.createFile(path)

    // Desired POSIX permissions: owner read/write, group read, others none
    val permissions = setOf(
        PosixFilePermission.OWNER_READ,
        PosixFilePermission.OWNER_WRITE,
        PosixFilePermission.GROUP_READ
    )

    // Apply the permissions
    path.setPosixFilePermissions(permissions)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/set-posix-file-permissions.html)

    