

# getLastModifiedTime

Returns the last modified time of the file located by this path.

```kotlin
inline fun Path.getLastModifiedTime(vararg options: LinkOption): FileTime(source)
```

```kotlin
import kotlin.io.path.Path
import kotlin.io.path.getLastModifiedTime
import java.nio.file.LinkOption

fun main() {
    val path = Path("example.txt")          // path to your file
    val lastModified = path.getLastModifiedTime()   // default: follow symbolic links
    println("Last modified time of $path: $lastModified")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/get-last-modified-time.html)

    