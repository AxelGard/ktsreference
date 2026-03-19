

# copyRecursively

Copies this file with all its children to the specified destination target path. If some directories on the way to the destination are missing, then they will be created.

```kotlin
@IgnorableReturnValuefun File.copyRecursively(target: File, overwrite: Boolean = false, onError: (File, IOException) -> OnErrorAction = { _, exception -> throw exception }): Boolean(source)
```

```kotlin
import java.io.File
import java.io.IOException
import kotlin.io.copyRecursively
import kotlin.io.onErrorAction

fun main() {
    val srcDir = File("src")
    val dstDir = File("dst")

    // Create some test files in the source directory
    srcDir.mkdirs()
    File(srcDir, "file1.txt").writeText("Hello")
    File(srcDir, "subdir/file2.txt").apply { parentFile.mkdirs(); writeText("World") }

    // Copy the directory recursively, overwrite if it exists, and handle errors
    val success = srcDir.copyRecursively(
        target = dstDir,
        overwrite = true,
        onError = { file, exc ->
            println("Failed to copy $file: ${exc.message}")
            OnErrorAction.Continue  // keep copying the rest
        }
    )

    println("Copy operation completed: $success")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/copy-recursively.html)

    