

# toPath

Converts this URI to a Path object.

```kotlin
inline fun URI.toPath(): Path(source)
```

```kotlin
import java.net.URI
import kotlin.io.path.toPath

fun main() {
    val uri = URI("file:///tmp/example.txt")
    val path = uri.toPath()
    println("Converted Path: $path")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/to-path.html)

    