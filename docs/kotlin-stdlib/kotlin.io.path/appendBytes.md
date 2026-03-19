

# appendBytes

Appends an array of bytes to the content of this file.

```kotlin
inline fun Path.appendBytes(array: ByteArray)(source)
```

```kotlin
import java.nio.file.Paths
import kotlin.io.path.appendBytes
import kotlin.io.path.readText

fun main() {
    val path = Paths.get("demo.txt")

    // Append first chunk of bytes
    val firstChunk = "Hello, ".toByteArray(Charsets.UTF_8)
    path.appendBytes(firstChunk)

    // Append second chunk of bytes
    val secondChunk = "world!".toByteArray(Charsets.UTF_8)
    path.appendBytes(secondChunk)

    // Verify the result
    println(path.readText())   // Prints: Hello, world!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.path/append-bytes.html)

    