

# inputStream

Constructs a new FileInputStream of this file and returns it as a result.

```kotlin
inline fun File.inputStream(): FileInputStream(source)
```

```kotlin
import java.io.File

fun main() {
    val file = File("example.txt")
    // Open a FileInputStream using the inline extension function
    file.inputStream().use { input ->
        val bytes = input.readBytes()
        println("Read ${bytes.size} bytes from ${file.name}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/input-stream.html)

    