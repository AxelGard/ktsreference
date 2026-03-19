

# relativeTo

Calculates the relative path for this file from base file. Note that the base file is treated as a directory. If this file matches the base file, then a File with empty path will be returned.

```kotlin
fun File.relativeTo(base: File): File(source)
```

```kotlin
import java.io.File

fun main() {
    val base = File("/home/user/projects")
    val file = File("/home/user/projects/src/main/kotlin/Example.kt")

    val relative = file.relativeTo(base)
    println(relative)   // prints: src/main/kotlin/Example.kt
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/relative-to.html)

    