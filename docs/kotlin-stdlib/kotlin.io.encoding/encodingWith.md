

# encodingWith

Returns an output stream that encodes bytes using the specified base64 encoding and writes the result to this output stream. Please refer to Base64 documentation for more details on the encoding itself.

```kotlin
@ExperimentalEncodingApifun OutputStream.encodingWith(base64: Base64): OutputStream(source)
```

```kotlin
import java.io.ByteArrayOutputStream
import kotlin.io.encoding.Base64
import kotlin.io.encoding.ExperimentalEncodingApi
import kotlin.io.encoding.encodingWith

@OptIn(ExperimentalEncodingApi::class)
fun main() {
    val text = "Hello, Kotlin!"
    val data = text.toByteArray()

    val baos = ByteArrayOutputStream()
    val encodedOut = baos.encodingWith(Base64.DEFAULT)

    encodedOut.write(data)
    encodedOut.close()

    val base64Bytes = baos.toByteArray()
    println(String(base64Bytes))   // prints the Base64‑encoded string
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io.encoding/encoding-with.html)

    