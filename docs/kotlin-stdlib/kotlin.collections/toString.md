

# toString

Converts the contents of this byte array to a string using the specified charset.

```kotlin
inline fun ByteArray.toString(charset: Charset): String(source)
```

```kotlin
import java.nio.charset.Charset

fun main() {
    val byteArray = "Hello, Kotlin!" .toByteArray(Charsets.UTF_8)
    val decodedString = byteArray.toString(Charsets.UTF_8)
    println(decodedString)   // prints: Hello, Kotlin!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-string.html)

    