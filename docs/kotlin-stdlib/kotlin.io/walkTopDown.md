

# walkTopDown

Gets a sequence for visiting this directory and all its content in top-down order. Depth-first search is used and directories are visited before all their files.

```kotlin
fun File.walkTopDown(): FileTreeWalk(source)
```

```kotlin
import java.io.File

fun main() {
    val root = File("src")          // Replace with the directory you want to walk

    // Walk the directory tree in top‑down order
    root.walkTopDown()
        .forEach { file ->
            // Print each directory before its files
            if (file.isDirectory) {
                println("📁 ${file.relativeTo(root)}")
            } else {
                println("    📄 ${file.relativeTo(root)}")
            }
        }
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/walk-top-down.html)

    