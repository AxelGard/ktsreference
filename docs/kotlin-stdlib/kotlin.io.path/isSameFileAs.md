

# isSameFileAs

Checks if the file located by this path points to the same file or directory as other.

```kotlin
inline fun Path.isSameFileAs(other: Path): Boolean(source)
```

```kotlin
import java.nio.file.Paths

fun main() {
    val pathA = Paths.get("example.txt")
    val pathB = Paths.get("example.txt")   // same file reference
    val pathC = Paths.get("different.txt") // different file

    println("pathA is same as pathB: ${pathA.isSameFileAs(pathB)}") // true
    println("pathA is same as pathC: ${pathA.isSameFileAs(pathC)}") // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/is-same-file-as.html)

    