

# createLinkPointingTo

Creates a new link (directory entry) located by this path for the existing file target.

```kotlin
@IgnorableReturnValueinline fun Path.createLinkPointingTo(target: Path): Path(source)
```

```kotlin
import java.nio.file.Files
import kotlin.io.path.createLinkPointingTo

fun main() {
    // Create a temporary target file
    val target = Files.createTempFile("target", ".txt")

    // Determine the link location (same directory, different name)
    val link = target.parent.resolve("linkToTarget")

    // Create the link pointing to the target
    link.createLinkPointingTo(target)

    println("Link created at ${link.toAbsolutePath()} → ${target.toAbsolutePath()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/create-link-pointing-to.html)

    