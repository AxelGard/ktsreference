

# extension

Returns the extension of this path (not including the dot), or an empty string if it doesn't have one.

```kotlin
val Path.extension: String(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.extension

fun main() {
    val file = Paths.get("example.txt")
    println(file.extension)   // prints: txt

    val hidden = Paths.get(".env")
    println(hidden.extension) // prints: (empty string)

    val archive = Paths.get("archive.tar.gz")
    println(archive.extension) // prints: gz
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/extension.html)

    