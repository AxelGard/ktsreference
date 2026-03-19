

# exists

Checks if the file located by this path exists.

```kotlin
inline fun Path.exists(vararg options: LinkOption): Boolean(source)
```

```kotlin
import java.nio.file.*
import kotlin.io.path.*

fun main() {
    val filePath = Paths.get("example.txt")

    // Check if the file exists
    if (filePath.exists()) {
        println("File exists.")
    } else {
        println("File does not exist.")
    }

    // Check if the file exists without following symbolic links
    if (filePath.exists(LinkOption.NOFOLLOW_LINKS)) {
        println("File exists (link options applied).")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/exists.html)

    