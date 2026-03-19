

# writeBytes

Writes an array of bytes to this file.

```kotlin
inline fun Path.writeBytes(array: ByteArray, vararg options: OpenOption)(source)
```

```kotlin
import java.nio.file.*

fun main() {
    // Path where the file will be written
    val path = Paths.get("example.txt")

    // Bytes to write
    val data = "Hello, Kotlin!".toByteArray(Charsets.UTF_8)

    // Write the bytes, creating the file if it doesn't exist and truncating if it does
    path.writeBytes(data, StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/write-bytes.html)

    