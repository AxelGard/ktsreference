

# invariantSeparatorsPath

Use invariantSeparatorsPathString property instead.

```kotlin
@ExperimentalPathApival Path.invariantSeparatorsPath: String(source)
```

```kotlin
import kotlin.io.path.*
import kotlin.io.path.ExperimentalPathApi

@OptIn(ExperimentalPathApi::class)
fun main() {
    val path = Paths.get("folder", "subfolder", "file.txt")
    val invariantPath = path.invariantSeparatorsPath
    println(invariantPath)   // e.g., "folder/subfolder/file.txt"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/invariant-separators-path.html)

    