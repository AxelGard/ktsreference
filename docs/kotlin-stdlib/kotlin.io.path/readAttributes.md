

# readAttributes

Reads a file's attributes of the specified type A in bulk.

```kotlin
inline fun <A : BasicFileAttributes> Path.readAttributes(vararg options: LinkOption): A(source)
```

```kotlin
import java.nio.file.Paths
import java.nio.file.attribute.BasicFileAttributes
import kotlin.io.path.readAttributes

fun main() {
    val path = Paths.get("example.txt")
    val attrs: BasicFileAttributes = path.readAttributes()

    println("Size: ${attrs.size()}")
    println("Creation time: ${attrs.creationTime()}")
    println("Last modified time: ${attrs.lastModifiedTime()}")
    println("Is regular file: ${attrs.isRegularFile}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/read-attributes.html)

    