

# writeBytes

Sets the content of this file as an array of bytes. If this file already exists, it becomes overwritten.

```kotlin
fun File.writeBytes(array: ByteArray)(source)
```

```kotlin
import java.io.File

fun main() {
    // Create or overwrite the file "output.bin"
    val file = File("output.bin")

    // Prepare some bytes to write
    val bytes = byteArrayOf(0x48, 0x65, 0x6C, 0x6C, 0x6F) // "Hello" in ASCII

    // Write the byte array to the file
    file.writeBytes(bytes)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/write-bytes.html)

    