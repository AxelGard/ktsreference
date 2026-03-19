

# charset

Returns a named charset with the given charsetName name.

```kotlin
inline fun charset(charsetName: String): Charset(source)
```

```kotlin
import java.nio.charset.Charset

fun main() {
    // Convert a string to bytes using a specific charset
    val bytes = "Hello, 世界".toByteArray(charset("UTF-8"))

    // Convert the bytes back to a string using the same charset
    val decoded = String(bytes, charset("UTF-8"))

    println(decoded) // Output: Hello, 世界
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/charset.html)

    