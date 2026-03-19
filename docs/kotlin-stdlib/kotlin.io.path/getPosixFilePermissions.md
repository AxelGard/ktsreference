

# getPosixFilePermissions

Returns the POSIX file permissions of the file located by this path.

```kotlin
inline fun Path.getPosixFilePermissions(vararg options: LinkOption): Set<PosixFilePermission>(source)
```

```kotlin
import java.nio.file.*
import kotlin.io.path.*

fun main() {
    val path = Path.of("example.txt")
    val permissions: Set<PosixFilePermission> = path.getPosixFilePermissions()
    println("Permissions for $path: $permissions")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/get-posix-file-permissions.html)

    