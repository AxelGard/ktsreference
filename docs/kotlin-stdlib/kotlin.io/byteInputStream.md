

# byteInputStream

Creates a new byte input stream for the string.

```kotlin
inline fun String.byteInputStream(charset: Charset = Charsets.UTF_8): ByteArrayInputStream(source)
```

```kotlin
import java.io.ByteArrayInputStream

fun main() {
    // Create a byte input stream from a string
    val stream: ByteArrayInputStream = "Hello, Kotlin!".byteInputStream()

    // Read all bytes from the stream
    val bytes = stream.readBytes()

    // Convert bytes back to string to verify
    println(String(bytes))   // Output: Hello, Kotlin!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/byte-input-stream.html)

    