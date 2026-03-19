

# invariantSeparatorsPathString

Returns the string representation of this path using the invariant separator '/' to separate names in the path.

```kotlin
val Path.invariantSeparatorsPathString: String(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.invariantSeparatorsPathString

fun main() {
    val path = Paths.get("folder", "subfolder", "file.txt")
    println(path.invariantSeparatorsPathString)  // Prints: folder/subfolder/file.txt
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/invariant-separators-path-string.html)

    