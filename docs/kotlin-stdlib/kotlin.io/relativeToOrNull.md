

# relativeToOrNull

Calculates the relative path for this file from base file. Note that the base file is treated as a directory. If this file matches the base file, then a File with empty path will be returned.

```kotlin
fun File.relativeToOrNull(base: File): File?(source)
```

```kotlin
import java.io.File

fun main() {
    val base = File("/Users/username/projects")
    val file = File("/Users/username/projects/src/main.kt")

    // Relative path from the base directory
    val relative = file.relativeToOrNull(base)
    println(relative?.path)          // prints: src/main.kt

    // When the file is not under the base directory, result is null
    val other = File("/Users/otheruser/projects/main.kt")
    println(other.relativeToOrNull(base))  // prints: null

    // When the file is exactly the base directory, result is a File with empty path
    val same = File("/Users/username/projects")
    println(same.relativeToOrNull(base))   // prints: .
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/relative-to-or-null.html)

    