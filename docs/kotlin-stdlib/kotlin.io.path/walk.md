

# walk

Returns a sequence of paths for visiting this directory and all its contents.

```kotlin
fun Path.walk(vararg options: PathWalkOption): Sequence<Path>(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.*

fun main() {
    val root = Paths.get("src")

    root.walk()              // visits root and all its sub‑directories
        .filter { it.isRegularFile() }  // keep only regular files
        .forEach { println(it) }       // print each file path
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/walk.html)

    