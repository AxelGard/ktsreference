

# forEachBlock

Reads file by byte blocks and calls action for each block read. Block has default size which is implementation-dependent. This functions passes the byte array and amount of bytes in the array to the action function.

```kotlin
fun File.forEachBlock(action: (buffer: ByteArray, bytesRead: Int) -> Unit)(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("input.txt")
    var totalBytes = 0

    file.forEachBlock { buffer, bytesRead ->
        // Do something with the bytes that were read
        totalBytes += bytesRead
        println("Read block of size: $bytesRead")
    }

    println("Total bytes read: $totalBytes")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/for-each-block.html)

    