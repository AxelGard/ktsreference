

# readSymbolicLink

Reads the target of a symbolic link located by this path.

```kotlin
inline fun Path.readSymbolicLink(): Path(source)
```

```kotlin
import java.nio.file.Files
import kotlin.io.path.Path
import kotlin.io.path.readSymbolicLink
import kotlin.io.path.writeText

fun main() {
    // Create a target file
    val target = Path("target.txt")
    target.writeText("Hello, world!")

    // Create a symbolic link pointing to the target file
    val link = Path("link.txt")
    Files.createSymbolicLink(link, target)

    // Read the link's target using the Kotlin extension
    val resolved: Path = link.readSymbolicLink()

    println("Link '$link' points to '$resolved'")

    // Clean up
    Files.deleteIfExists(link)
    Files.deleteIfExists(target)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/read-symbolic-link.html)

    