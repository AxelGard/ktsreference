

# absolute

Converts this possibly relative path to an absolute path.

```kotlin
inline fun Path.absolute(): Path(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.absolute

fun main() {
    val relativePath = Paths.get("docs/readme.md")
    val absolutePath = relativePath.absolute()
    println(absolutePath)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/absolute.html)

    