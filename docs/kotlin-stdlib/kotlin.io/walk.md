

# walk

Gets a sequence for visiting this directory and all its content.

```kotlin
fun File.walk(direction: FileWalkDirection = FileWalkDirection.TOP_DOWN): FileTreeWalk(source)
```

```kotlin
import java.io.File

fun main() {
    val directory = File("exampleDir")
    // Walk the directory tree (top‑down by default) and print each file/directory
    directory.walk().forEach { file ->
        println(file.path)
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/walk.html)

    