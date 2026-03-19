

# visitFileTree

Visits this directory and all its contents with the specified visitor.

```kotlin
fun Path.visitFileTree(visitor: FileVisitor<Path>, maxDepth: Int = Int.MAX_VALUE, followLinks: Boolean = false)(source)
```

```kotlin
import java.nio.file.*
import java.nio.file.attribute.BasicFileAttributes

fun main() {
    val dir = Paths.get("src/main/java")  // change to the directory you want to traverse

    dir.visitFileTree(object : SimpleFileVisitor<Path>() {
        override fun visitFile(file: Path, attrs: BasicFileAttributes): FileVisitResult {
            println("Visited file: $file")
            return FileVisitResult.CONTINUE
        }

        override fun preVisitDirectory(dir: Path, attrs: BasicFileAttributes): FileVisitResult {
            println("Entering directory: $dir")
            return FileVisitResult.CONTINUE
        }

        override fun postVisitDirectory(dir: Path, exc: IOException?): FileVisitResult {
            println("Leaving directory: $dir")
            return FileVisitResult.CONTINUE
        }

        override fun visitFileFailed(file: Path, exc: IOException): FileVisitResult {
            println("Failed to visit file: $file (${exc.message})")
            return FileVisitResult.CONTINUE
        }
    })
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/visit-file-tree.html)

    