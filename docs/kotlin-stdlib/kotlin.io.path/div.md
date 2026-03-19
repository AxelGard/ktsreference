

# div

Resolves the given other path against this path.

```kotlin
inline operator fun Path.div(other: Path): Path(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.div

fun main() {
    val base = Paths.get("/usr/local")
    val sub  = Paths.get("bin")

    val fullPath = base / sub   // same as base.div(sub)

    println(fullPath)  // prints: /usr/local/bin
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/div.html)

    