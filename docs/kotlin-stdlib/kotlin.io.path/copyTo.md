

# copyTo

Copies a file or directory located by this path to the given target path.

```kotlin
@IgnorableReturnValueinline fun Path.copyTo(target: Path, overwrite: Boolean = false): Path(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.copyTo
import kotlin.io.path.Path

val source: Path = Paths.get("src/main/resources/config.yaml")
val target: Path = Paths.get("build/config.yaml")

source.copyTo(target, overwrite = true)
println("Copied $source to $target")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/copy-to.html)

    