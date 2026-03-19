

# fileAttributesViewOrNull

Returns a file attributes view of a given type V or null if the requested attribute view type is not available.

```kotlin
inline fun <V : FileAttributeView> Path.fileAttributesViewOrNull(vararg options: LinkOption): V?(source)
```

```kotlin
import java.nio.file.Path
import java.nio.file.Paths
import java.nio.file.attribute.PosixFileAttributeView
import kotlin.io.path.fileAttributesViewOrNull

fun main() {
    val path: Path = Paths.get("sample.txt")

    // Attempt to obtain a PosixFileAttributeView.  
    // The result will be null if the file system does not support POSIX attributes.
    val posixView: PosixFileAttributeView? = path.fileAttributesViewOrNull()

    if (posixView != null) {
        val attrs = posixView.readAttributes()
        println("Owner: ${attrs.owner()}")
        println("Permissions: ${attrs.permissions()}")
    } else {
        println("PosixFileAttributeView is not available for this file system.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/file-attributes-view-or-null.html)

    