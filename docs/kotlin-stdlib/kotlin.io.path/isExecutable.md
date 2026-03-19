

# isExecutable

Checks if the file located by this path exists and is executable.

```kotlin
inline fun Path.isExecutable(): Boolean(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.isExecutable

fun main() {
    val path = Paths.get("script.sh")   // Path to the file you want to check
    if (path.isExecutable()) {
        println("$path is executable.")
    } else {
        println("$path is not executable.")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/is-executable.html)

    