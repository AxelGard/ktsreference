

# nameWithoutExtension

Returns the name of this file or directory without an extension, or an empty string if this path has zero path elements.

```kotlin
val Path.nameWithoutExtension: String(source)
```

```kotlin
import kotlin.io.path.Path
import kotlin.io.path.nameWithoutExtension

fun main() {
    val file = Path("documents/report.pdf")
    println(file.nameWithoutExtension) // Output: report

    val dir = Path("images")
    println(dir.nameWithoutExtension)   // Output: images

    val empty = Path("")
    println(empty.nameWithoutExtension) // Output: 
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/name-without-extension.html)

    