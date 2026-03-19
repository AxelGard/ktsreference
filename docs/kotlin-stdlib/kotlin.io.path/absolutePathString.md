

# absolutePathString

Converts this possibly relative path to an absolute path and returns its string representation.

```kotlin
inline fun Path.absolutePathString(): String(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.absolutePathString

fun main() {
    val relative = Paths.get("src/main/kotlin")
    val absolute = relative.absolutePathString()
    println("Absolute path: $absolute")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/absolute-path-string.html)

    