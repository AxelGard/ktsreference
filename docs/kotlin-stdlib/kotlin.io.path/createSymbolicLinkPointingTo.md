

# createSymbolicLinkPointingTo

Creates a new symbolic link located by this path to the given target.

```kotlin
@IgnorableReturnValueinline fun Path.createSymbolicLinkPointingTo(target: Path, vararg attributes: FileAttribute<*>): Path(source)
```

```kotlin
import java.nio.file.Path
import kotlin.io.path.createSymbolicLinkPointingTo
import kotlin.io.path.writeText

fun main() {
    val target = Path.of("target.txt")   // the file we want the symlink to point to
    val link   = Path.of("link.txt")     // the symlink that will be created

    // Create the target file and write some content
    target.writeText("Hello, world!")

    // Create a symbolic link at 'link.txt' that points to 'target.txt'
    link.createSymbolicLinkPointingTo(target)

    println("Symlink created: $link → $target")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/create-symbolic-link-pointing-to.html)

    