

# decodingWith

Returns an input stream that decodes symbols from this input stream using the specified base64 encoding. Please refer to Base64 documentation for more details on the encoding itself.

```kotlin
@ExperimentalEncodingApifun InputStream.decodingWith(base64: Base64): InputStream(source)
```

```kotlin
import kotlin.io.encoding.Base64
import kotlin.io.encoding.ExperimentalEncodingApi

@OptIn(ExperimentalEncodingApi::class)
fun main() {
    // A Base64‑encoded string
    val base64Text = "SGVsbG8gd29ybGQh"

    // Decode it using decodingWith
    val decodedString = base64Text
        .toByteArray(Charsets.UTF_8)           // Convert to bytes
        .inputStream()                         // InputStream from the bytes
        .decodingWith(Base64.DEFAULT)          // Wrap with a decoding stream
        .readBytes()                           // Read the decoded bytes
        .decodeToString()                      // Convert back to a string

    println(decodedString)   // Prints: Hello world!
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.encoding/decoding-with.html)

    