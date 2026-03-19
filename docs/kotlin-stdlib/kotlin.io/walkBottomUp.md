

# walkBottomUp

Gets a sequence for visiting this directory and all its content in bottom-up order. Depth-first search is used and directories are visited after all their files.

```kotlin
fun File.walkBottomUp(): FileTreeWalk(source)
```

```kotlin
import java.io.File

fun main() {
    // Replace with the path of the directory you want to traverse
    val rootDir = File("path/to/your/directory")

    rootDir.walkBottomUp()
        .filter { it.isFile }   // process only files
        .forEach { file ->
            println("Found file: ${file.relativeTo(rootDir)}")
        }
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/walk-bottom-up.html)

    