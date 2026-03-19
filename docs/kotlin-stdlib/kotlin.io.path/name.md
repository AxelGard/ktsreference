

# name

Returns the name of the file or directory denoted by this path as a string, or an empty string if this path has zero path elements.

```kotlin
val Path.name: String(source)
```

```kotlin
import java.nio.file.Path

fun main() {
    val path: Path = Path.of("/home/user/docs/report.pdf")
    println(path.name)   // prints "report.pdf"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/name.html)

    