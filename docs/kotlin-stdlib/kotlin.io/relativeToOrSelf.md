

# relativeToOrSelf

Calculates the relative path for this file from base file. Note that the base file is treated as a directory. If this file matches the base file, then a File with empty path will be returned.

```kotlin
fun File.relativeToOrSelf(base: File): File(source)
```

```kotlin
import java.io.File

fun main() {
    val base = File("project")
    val file1 = File("project/src/Main.kt")
    val file2 = File("project")   // same as base

    println(file1.relativeToOrSelf(base).path) // → "src/Main.kt"
    println(file2.relativeToOrSelf(base).path) // → "" (empty path)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/relative-to-or-self.html)

    