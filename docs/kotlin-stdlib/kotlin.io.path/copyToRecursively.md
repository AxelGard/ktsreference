

# copyToRecursively

Recursively copies this directory and its content to the specified destination target path. Note that if this function throws, partial copying may have taken place.

```kotlin
@ExperimentalPathApi@IgnorableReturnValuefun Path.copyToRecursively(target: Path, onError: (source: Path, target: Path, Exception) -> OnErrorResult = { _, _, exception -> throw exception }, followLinks: Boolean, overwrite: Boolean): Path(source)
```

```kotlin
import java.nio.file.Path
import kotlin.io.path.*

@ExperimentalPathApi
fun main() {
    val source: Path = Path.of("srcDir")
    val target: Path = Path.of("destDir")

    source.copyToRecursively(
        target = target,
        onError = { src, tgt, ex ->
            println("Failed to copy $src to $tgt: ${ex.message}")
            OnErrorResult.SKIP
        },
        followLinks = true,
        overwrite = true
    )
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/copy-to-recursively.html)

    