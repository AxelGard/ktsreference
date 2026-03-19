

# resolve

Adds relative file to this, considering this as a directory. If relative has a root, relative is returned back. For instance, File("/foo/bar").resolve(File("gav")) is File("/foo/bar/gav"). This function is complementary with relativeTo, so f.resolve(g.relativeTo(f)) == g should be always true except for different roots case.

```kotlin
fun File.resolve(relative: File): File(source)
```

```kotlin
import java.io.File

fun main() {
    val base = File("/foo/bar")          // a directory
    val relative = File("gav")           // relative file
    val resolved = base.resolve(relative)

    println(resolved)   // prints: /foo/bar/gav
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/resolve.html)

    