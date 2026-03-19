

# readBytes

Gets the entire content of this file as a byte array.

```kotlin
fun File.readBytes(): ByteArray(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("example.txt")
    val bytes = file.readBytes()
    println("Read ${bytes.size} bytes")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/read-bytes.html)

    