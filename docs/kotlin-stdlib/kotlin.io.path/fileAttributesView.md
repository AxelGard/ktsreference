

# fileAttributesView

Returns a file attributes view of a given type V or throws an UnsupportedOperationException if the requested attribute view type is not available..

```kotlin
inline fun <V : FileAttributeView> Path.fileAttributesView(vararg options: LinkOption): V(source)
```

```kotlin
import java.nio.file.Paths
import java.nio.file.LinkOption
import java.nio.file.attribute.BasicFileAttributeView
import java.nio.file.attribute.PosixFileAttributeView

fun main() {
    val path = Paths.get("example.txt")

    // Get a BasicFileAttributeView
    val basicView = path.fileAttributesView<BasicFileAttributeView>()
    val basicAttrs = basicView.readAttributes()
    println("Size: ${basicAttrs.size()}")
    println("Last modified: ${basicAttrs.lastModifiedTime()}")

    // Get a PosixFileAttributeView (if supported on the OS)
    val posixView = path.fileAttributesView<PosixFileAttributeView>()
    val posixAttrs = posixView.readAttributes()
    println("Permissions: ${posixAttrs.permissions()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/file-attributes-view.html)

    