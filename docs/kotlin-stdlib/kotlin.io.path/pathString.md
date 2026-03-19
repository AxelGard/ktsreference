

# pathString

Returns the string representation of this path.

```kotlin
val Path.pathString: String(source)
```

```kotlin
import java.nio.file.Path
import kotlin.io.path.pathString

fun main() {
    val path: Path = Path.of("src", "main", "kotlin", "Example.kt")
    println(path.pathString)  // Output: src/main/kotlin/Example.kt
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/path-string.html)

    