

# copyTo

Copies this stream to the given output stream, returning the number of bytes copied

```kotlin
@IgnorableReturnValuefun InputStream.copyTo(out: OutputStream, bufferSize: Int = DEFAULT_BUFFER_SIZE): Long(source)
```

```kotlin
import java.io.File

fun copyExample() {
    val sourceFile = File("input.txt")
    val destFile   = File("output.txt")

    sourceFile.inputStream().use { input ->
        destFile.outputStream().use { output ->
            val bytesCopied = input.copyTo(output)
            println("Copied $bytesCopied bytes.")
        }
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/copy-to.html)

    