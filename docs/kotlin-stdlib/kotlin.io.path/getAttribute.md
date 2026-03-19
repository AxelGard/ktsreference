

# getAttribute

Reads the value of a file attribute.

```kotlin
inline fun Path.getAttribute(attribute: String, vararg options: LinkOption): Any?(source)
```

```kotlin
import java.nio.file.Paths
import java.nio.file.LinkOption
import kotlin.io.path.getAttribute

fun main() {
    val path = Paths.get("sample.txt")
    val size = path.getAttribute("size", LinkOption.NOFOLLOW_LINKS) as? Long
    println("Size: $size bytes")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/get-attribute.html)

    