

# fileVisitor

Builds a FileVisitor whose implementation is defined in builderAction.

```kotlin
fun fileVisitor(builderAction: FileVisitorBuilder.() -> Unit): FileVisitor<Path>(source)
```

```kotlin
import java.nio.file.*
import java.nio.file.attribute.*
import kotlin.io.path.fileVisitor

fun main() {
    val startPath = Paths.get(".")

    val visitor = fileVisitor {
        preVisitDirectory { dir, attrs ->
            println("Entering directory: $dir")
            FileVisitResult.CONTINUE
        }
        visitFile { file, attrs ->
            println("Visited file: $file")
            FileVisitResult.CONTINUE
        }
        postVisitDirectory { dir, exc ->
            println("Leaving directory: $dir")
            FileVisitResult.CONTINUE
        }
        visitFileFailed { file, exc ->
            println("Failed to visit $file: ${exc.message}")
            FileVisitResult.CONTINUE
        }
    }

    Files.walkFileTree(startPath, visitor)
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/file-visitor.html)

    