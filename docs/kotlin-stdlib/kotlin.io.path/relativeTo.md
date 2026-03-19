

# relativeTo

Calculates the relative path for this path from a base path.

```kotlin
fun Path.relativeTo(base: Path): Path(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.relativeTo

fun main() {
    val base = Paths.get("/home/user/docs")
    val file = Paths.get("/home/user/docs/project/readme.md")

    val relative = file.relativeTo(base)
    println(relative) // outputs: project/readme.md
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/relative-to.html)

    