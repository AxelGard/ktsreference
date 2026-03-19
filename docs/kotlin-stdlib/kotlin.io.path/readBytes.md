

# readBytes

Gets the entire content of this file as a byte array.

```kotlin
inline fun Path.readBytes(): ByteArray(source)
```

```kotlin
import java.nio.file.Paths

fun main() {
    val path = Paths.get("example.txt")
    val bytes = path.readBytes()
    println(String(bytes))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/read-bytes.html)

    