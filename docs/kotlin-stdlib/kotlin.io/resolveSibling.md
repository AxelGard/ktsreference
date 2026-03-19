

# resolveSibling

Adds relative file to this parent directory. If relative has a root or this has no parent directory, relative is returned back. For instance, File("/foo/bar").resolveSibling(File("gav")) is File("/foo/gav").

```kotlin
fun File.resolveSibling(relative: File): File(source)
```

```kotlin
import java.io.File

fun main() {
    val original = File("/foo/bar")
    val sibling = File("gav")
    val resolved = original.resolveSibling(sibling)
    println(resolved) // prints: /foo/gav
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/resolve-sibling.html)

    