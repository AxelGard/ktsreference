

# endsWith

Determines whether this file path ends with the path of other file.

```kotlin
fun File.endsWith(other: File): Boolean(source)
```

```kotlin
import java.io.File

fun main() {
    val parentDir = File("/home/user/documents")
    val file1 = File("/home/user/documents/report.pdf")
    val file2 = File("/home/user/music/song.mp3")

    println(file1.endsWith(parentDir)) // true
    println(file2.endsWith(parentDir)) // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/ends-with.html)

    