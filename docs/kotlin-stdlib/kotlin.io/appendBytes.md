

# appendBytes

Appends an array of bytes to the content of this file.

```kotlin
fun File.appendBytes(array: ByteArray)(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("example.txt")

    // Create file and write initial content
    file.writeText("Hello")

    // Prepare bytes to append
    val bytesToAppend = " World!".toByteArray()

    // Append bytes to the file
    file.appendBytes(bytesToAppend)

    // Read and print content
    println(file.readText()) // Output: Hello World!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/append-bytes.html)

    