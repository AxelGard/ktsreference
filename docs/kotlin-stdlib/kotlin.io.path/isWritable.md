

# isWritable

Checks if the file located by this path exists and is writable.

```kotlin
inline fun Path.isWritable(): Boolean(source)
```

```kotlin
import java.nio.file.Path
import kotlin.io.path.isWritable

fun main() {
    val path = Path.of("example.txt")

    if (path.isWritable()) {
        println("$path is writable")
    } else {
        println("$path is not writable")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/is-writable.html)

    