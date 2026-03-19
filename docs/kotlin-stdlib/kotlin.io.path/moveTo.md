

# moveTo

Moves or renames the file located by this path to the target path.

```kotlin
@IgnorableReturnValueinline fun Path.moveTo(target: Path, vararg options: CopyOption): Path(source)
```

```kotlin
import java.nio.file.Paths
import java.nio.file.StandardCopyOption
import kotlin.io.path.moveTo

fun main() {
    val source = Paths.get("example.txt")          // path of the file to move
    val target = Paths.get("backup", "example.txt") // new location / name

    // Move (or rename) the file, replacing any existing file at the target location
    source.moveTo(target, StandardCopyOption.REPLACE_EXISTING)
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/move-to.html)

    